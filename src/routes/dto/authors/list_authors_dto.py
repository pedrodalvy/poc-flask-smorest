from marshmallow import Schema
from marshmallow.fields import String, Integer


class ListAuthorsResponseDTO(Schema):
    id = Integer(dump_only=True, example=1)
    name = String(required=True, example="John Doe")
