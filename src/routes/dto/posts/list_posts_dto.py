from marshmallow import Schema
from marshmallow.fields import Integer, String, Nested


class ListPostsRequestDTO(Schema):
    author_id = Integer(required=False, example="1")


class AuthorResponseDTO(Schema):
    id = Integer(required=True, example="1")
    name = String(required=True, example="John Doe")


class ListPostsResponseDTO(Schema):
    id = Integer(required=True, example="1")
    title = String(required=True, example="My first post")
    content = String(required=True, example="This is my first post")
    author = Nested(AuthorResponseDTO, required=True)
