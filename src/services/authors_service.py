from typing import List, Dict

from src.entities.author import Author

authors_list: List[Author] = []


def list_authors() -> List[Author]:
    return authors_list


def get_author(author_id: int) -> Author:
    author = next((author for author in authors_list if author.id == author_id), None)
    return author


def delete_author(author_id: int) -> Author:
    author = next((author for author in authors_list if author.id == author_id), None)
    authors_list.remove(author)
    return author


def update_author(author_id: int, dto: Dict[str, str]) -> Author:
    author = next((author for author in authors_list if author.id == author_id), None)
    author.name = dto.get("name")
    return author


def create_author(dto: Dict[str, str]) -> Author:
    author_id = len(authors_list) + 1
    author_name = dto.get("name")

    author = Author(name=author_name, id=author_id)
    authors_list.append(author)
    return author
