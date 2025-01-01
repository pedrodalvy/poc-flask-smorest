from typing import List, Dict

from src.entities.post import Post

posts_list: List[Post] = []


def list_posts(input_dto: Dict[str, str]) -> List[Post]:
    author_id = input_dto.get("author_id")

    if author_id:
        return [post for post in posts_list if post.author_id == author_id]

    return posts_list


def create_post(input_dto: Dict[str, str]) -> Post:
    post_id = len(posts_list) + 1
    post_title = input_dto.get("title")
    post_content = input_dto.get("content")
    post_author_id = input_dto.get("author_id")

    post = Post(id=post_id, title=post_title, content=post_content, author_id=post_author_id)
    posts_list.append(post)
    return post
