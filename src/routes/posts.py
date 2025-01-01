from http import HTTPStatus, HTTPMethod
from typing import Dict

from flask_smorest import Blueprint

from src.routes.dto.posts.create_post_dto import CreatePostResponseDTO, CreatePostRequestDTO
from src.routes.dto.posts.list_posts_dto import ListPostsResponseDTO, ListPostsRequestDTO
from src.services import posts_service

posts_blp = Blueprint("Posts", __name__, url_prefix="/posts", description="Operations on posts")


@posts_blp.route("/", methods=[HTTPMethod.GET])
@posts_blp.response(HTTPStatus.OK, ListPostsResponseDTO(many=True))
@posts_blp.arguments(ListPostsRequestDTO, location="query")
def list_posts(input_dto: Dict[str, str]):
    return posts_service.list_posts(input_dto)


@posts_blp.route("/", methods=[HTTPMethod.POST])
@posts_blp.response(HTTPStatus.CREATED, CreatePostResponseDTO())
@posts_blp.arguments(CreatePostRequestDTO, location="json")
def create_post(input_dto: Dict[str, str]):
    return posts_service.create_post(input_dto)
