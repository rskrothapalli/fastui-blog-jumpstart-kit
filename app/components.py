
from typing import Protocol
from data_models import User, Blog, Article
import importlib


class Page(Protocol):
    def render(self, config: dict) -> str:
        pass

class BlogPage():
    def __init__(self, active_user: User) -> None:
        self.active_user = active_user

    def render(self, config: dict):
        blog = Blog(**config)
        template_module_str = f"templates.homepage_template_{blog.blog_template_id}"
        template_module = importlib.import_module(template_module_str)
        return template_module.template(self.active_user, blog)


class ArticlePage():
    def __init__(self, active_user: User) -> None:
        self.active_user = active_user

    def render(self, config: dict):
        article = Article(**config)

        template_module_str = f"templates.article_template_{article.article_template_id}"
        template_module = importlib.import_module(template_module_str)
        return template_module.template(self.active_user, article)


def generate_page(page_type: str = "Blog", current_user: dict = {}) -> Page:
    page: dict[str, type[Page]] = {
        "Blog": BlogPage,
        "Article": ArticlePage
    }

    return page[page_type](User(**current_user))

