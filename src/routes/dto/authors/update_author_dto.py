from marshmallow import Schema
from marshmallow.fields import String, Integer, DateTime


class UpdateAuthorRequestDTO(Schema):
    name = String(required=True, example="John Doe")


class UpdateAuthorResponseDTO(Schema):
    id = Integer(dump_only=True, example=1)
    name = String(required=True, example="John Doe")
    created_at = DateTime(dump_only=True, example="2022-01-01T00:00:00")
