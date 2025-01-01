from http import HTTPStatus, HTTPMethod
from typing import Dict

from flask_smorest import Blueprint

from src.routes.dto.authors.create_author_dto import CreateAuthorResponseDTO, CreateAuthorRequestDTO
from src.routes.dto.authors.delete_author_dto import DeleteAuthorResponseDTO
from src.routes.dto.authors.get_author_dto import GetAuthorResponseDTO
from src.routes.dto.authors.list_authors_dto import ListAuthorsResponseDTO
from src.routes.dto.authors.update_author_dto import UpdateAuthorResponseDTO, UpdateAuthorRequestDTO
from src.services import authors_service

authors_blp = Blueprint("Authors", __name__, url_prefix="/authors", description="Operations on authors")


@authors_blp.route("/", methods=[HTTPMethod.GET])
@authors_blp.response(HTTPStatus.OK, ListAuthorsResponseDTO(many=True))
def list_authors():
    return authors_service.list_authors()


@authors_blp.route("/", methods=[HTTPMethod.POST])
@authors_blp.response(HTTPStatus.CREATED, CreateAuthorResponseDTO())
@authors_blp.arguments(CreateAuthorRequestDTO, location="json")
def create_author(dto: Dict[str, str]):
    return authors_service.create_author(dto)


@authors_blp.route("/<int:author_id>", methods=[HTTPMethod.GET])
@authors_blp.response(HTTPStatus.OK, GetAuthorResponseDTO)
def get_author(author_id: int):
    return authors_service.get_author(author_id)


@authors_blp.route("/<int:author_id>", methods=[HTTPMethod.DELETE])
@authors_blp.response(HTTPStatus.OK, DeleteAuthorResponseDTO)
def delete_author(author_id):
    return authors_service.delete_author(author_id)


@authors_blp.route("/<int:author_id>", methods=[HTTPMethod.PUT])
@authors_blp.response(HTTPStatus.OK, UpdateAuthorResponseDTO)
@authors_blp.arguments(UpdateAuthorRequestDTO, location="json")
def update_author(dto: Dict[str, str], author_id: int):
    return authors_service.update_author(author_id, dto)
