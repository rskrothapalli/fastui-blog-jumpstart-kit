from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastui import FastUI, prebuilt_html, components as c
from yaml import safe_load, YAMLError
from contextlib import asynccontextmanager
from components import generate_page
import uvicorn
from fastapi.responses import HTMLResponse
from pathlib import Path

config = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    with open(Path(__file__).resolve().parent / "blog.yml", "r") as config_file:
        try:
            config["blog"] = safe_load(config_file)
            # Only pick one active user the first active user in the config
            config["active_user"] = [user for user in config["blog"]["users"] if user["status"] == 'active'][0]
            config["articles"] = [article for article in config["blog"]["articles"] if article['status'] == 'published'] 
        except YAMLError as exc:
            print(exc)
    print("Configuration loaded successfully")
    yield
    config.clear()


app = FastAPI(lifespan=lifespan)

articles_dir = Path(__file__).resolve().parent / "articles"
articles_dir.mkdir(parents=True, exist_ok=True)
app.mount("/articles", StaticFiles(directory=articles_dir), name="articles")

images_dir = Path(__file__).resolve().parent / "static" / "images"
app.mount("/images", StaticFiles(directory=images_dir), name="images")
app.mount("/article/images", StaticFiles(directory=images_dir), name="art_images")

@app.get("/api/", response_model=FastUI, response_model_exclude_none=True)
def home_page():
    return c.Page(components=generate_page("Blog", config["active_user"]).render(config["blog"]))


@app.get("/api/article/{article_id}", response_model=FastUI, response_model_exclude_none=True)
def post_page(article_id):
    article_config = [article for article in config["articles"] if article["article_id"]==int(article_id)][0]
    if not article_config:
        raise HTTPException(status_code=404, detail="Article not found")
    return c.Page(components=generate_page("Article", config["active_user"]).render(article_config))
    

@app.get('/{path:path}')
async def html_landing() -> HTMLResponse:
    """Simple HTML page which serves the React app, comes last as it matches all paths."""
    return HTMLResponse(prebuilt_html(title='FastUI Demo'))


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)