from fastui import components as c
from fastui.components.display import DisplayLookup
from fastui.events import GoToEvent
from data_models import User, Blog


def generate_social_links(user: User):
    snet_components = []
    for snet, snet_url in dict(user.social).items():
        img_component = c.Image(class_name='+ img-thumbnail me-2', src=f'images/{snet.lower()}.svg', height='34px', width='34px', on_click=GoToEvent(url=snet_url)),
        snet_components.append(img_component[0])
        snet_components.append(c.Text(text=snet))
        snet_components.append(c.Text(text=' | '))
    return snet_components


def template(user: User, blog: Blog):
    return [
            c.Navbar(title=user.name,
                    start_links=[c.Link(components=generate_social_links(user=user),
                                        on_click=GoToEvent(url="/"))], class_name="+ navbar-expand-lg bg-body-secondary h6"),
            c.Markdown(text="\n\n"),
            c.Heading(text=blog.blog_title, level=5, class_name="+ py-4"),
            c.Markdown(text=blog.sub_title, class_name="+ text-muted"),
            c.Markdown(text=blog.disclaimer, class_name="+ py-2 text-muted"),
            c.Table(
                data=[article for article in blog.articles  if article.status == 'published'],
                columns=[
                    DisplayLookup(field="title", title="Posts",
                                  on_click=GoToEvent(url="/article/{article_id}")),
                ],
            ) if blog.articles else c.Text(text="No articles found."),
        ]