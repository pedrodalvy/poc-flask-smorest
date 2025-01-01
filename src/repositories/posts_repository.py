from typing import List, Optional

from src.entities.post import Post
from src.repositories import authors_repository

posts_list: List[Post] = []


def list_posts(author_id: Optional[int]) -> List[Post]:
    posts = posts_list
    if author_id:
        posts = [post for post in posts_list if post.author_id == author_id]

    for post in posts:
        post.author = authors_repository.get_author(post.author_id)

    return posts


def create_post(post: Post) -> Post:
    post.id = len(posts_list) + 1
    posts_list.append(post)
    return post
