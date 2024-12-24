from marshmallow import Schema
from marshmallow.fields import String, Integer


class CreateAuthorRequestDTO(Schema):
    name = String(required=True, example="John Doe")


class CreateAuthorResponseDTO(Schema):
    id = Integer(required=True, example=1)
