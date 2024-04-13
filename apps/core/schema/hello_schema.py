from ninja import Schema


class HelloSchema(Schema):
    name: str


class HelloResponseSchema(Schema):
    message: str


class Error(Schema):
    message: str
