from pydantic import BaseModel, EmailStr
from typing import Optional

class Social(BaseModel):
    Github: Optional[str] = None
    LinkedIn: Optional[str] = None


class User(BaseModel):
    user_id: str
    name: str
    email: EmailStr
    avatar: Optional[str] = None
    access: str
    status: str
    social: Social


class Article(BaseModel):
    article_id: int
    title: str
    source_file: str
    article_template_id: int
    author_id: str
    status: str
    last_updated: str

class Blog(BaseModel):
    page_title: str
    blog_title: str
    sub_title: str
    disclaimer: str
    blog_template_id: int
    posts_per_page: int
    users: list[User]
    articles: list[Article]


