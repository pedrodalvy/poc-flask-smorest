from typing import List, Dict

from werkzeug.exceptions import NotFound

from src.entities.post import Post
from src.repositories import posts_repository, authors_repository


def list_posts(input_dto: Dict[str, str]) -> List[Post]:
    author_id = input_dto.get("author_id")
    return posts_repository.list_posts(author_id)


def create_post(input_dto: Dict[str, str]) -> Post:
    post_title = input_dto["title"]
    post_content = input_dto["content"]
    post_author_id = int(input_dto["author_id"])

    author = authors_repository.get_author(post_author_id)
    if not author:
        raise NotFound("Author not found")

    post = Post(title=post_title, content=post_content, author_id=post_author_id)
    return posts_repository.create_post(post)
