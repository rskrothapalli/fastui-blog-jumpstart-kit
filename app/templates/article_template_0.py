
import importlib
from fastui import components as c
from fastui.events import GoToEvent, BackEvent
from data_models import User, Article
from file_reader import read_content
from pathlib import Path

def generate_social_links(user: User):
    snet_components = []
    for snet, snet_url in dict(user.social).items():
        img_component = c.Image(class_name='+ img-thumbnail me-2', src=f'images/{snet.lower()}.svg', height='34px', width='34px', on_click=GoToEvent(url=snet_url)),
        snet_components.append(img_component[0])
        snet_components.append(c.Text(text=snet))
        snet_components.append(c.Text(text=' | '))
    return snet_components



def template(user: User, article: Article):
    return [
            c.Navbar(title=user.name,
                    start_links=[c.Link(components=generate_social_links(user=user),
                                        on_click=GoToEvent(url="/"))], class_name="+ navbar-expand-lg bg-body-secondary h6"),
            c.Markdown(text="\n\n"),
            c.Link(components=[c.Text(text='Home')], on_click=BackEvent(), class_name='+ py-4'),
            c.Heading(text=article.title, level=4, class_name='+ py-2'),
            c.Text(text="written by"),
            c.Link(components=[c.Text(text=user.name.upper())], on_click=GoToEvent(
                url=user.social.LinkedIn), class_name='+ container-sm small text-muted py-2'),
            c.Markdown(
                text=f"published on {article.last_updated}", class_name='+ small text-muted'),
            c.Div(components=[], class_name='+ py-2'),
            c.Markdown(text=read_content(
                f"articles/{article.source_file}"))
            if Path(article.source_file).suffix == '.md' else c.Div(components=importlib.import_module(f"articles.{Path(article.source_file.replace('/','.')).stem}").get_output()),
    ]


