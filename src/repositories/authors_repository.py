from typing import List, Optional

from src.entities.author import Author

authors_list: List[Author] = []


def list_authors() -> List[Author]:
    return authors_list


def get_author(author_id: int) -> Optional[Author]:
    for index, author in enumerate(authors_list):
        if author.id == author_id:
            return authors_list[index]

    return None


def delete_author(author_id: int) -> Optional[Author]:
    for index, author in enumerate(authors_list):
        if author.id == author_id:
            return authors_list.pop(index)

    return None


def update_author(author: Author) -> Author:
    for index, data in authors_list:
        if data.id == author.id:
            authors_list[index] = author

    return author


def create_author(author: Author) -> Author:
    author.id = len(authors_list) + 1
    authors_list.append(author)

    return author
