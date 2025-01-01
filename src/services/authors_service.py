from typing import List, Dict

from src.entities.author import Author
from src.repositories import authors_repository


def list_authors() -> List[Author]:
    return authors_repository.list_authors()


def get_author(author_id: int) -> Author:
    return authors_repository.get_author(author_id)


def delete_author(author_id: int) -> Author:
    return authors_repository.delete_author(author_id)


def update_author(author_id: int, dto: Dict[str, str]) -> Author:
    author = authors_repository.get_author(author_id)
    author.name = dto.get("name")
    return author


def create_author(dto: Dict[str, str]) -> Author:
    author = Author(name=dto.get("name"))
    return authors_repository.create_author(author)
