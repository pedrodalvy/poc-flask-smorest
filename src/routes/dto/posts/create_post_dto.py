from marshmallow import Schema
from marshmallow.fields import String, Integer


class CreatePostRequestDTO(Schema):
    title = String(required=True, example="My first post")
    content = String(required=True, example="This is my first post")
    author_id = Integer(required=True, example="1")


class CreatePostResponseDTO(Schema):
    id = Integer(required=True, example="1")
