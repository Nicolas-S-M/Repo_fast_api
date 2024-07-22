from pydantic import BaseModel


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    name: str
    age: int


class UserDB(UserSchema):
    id: int


class UserList(BaseModel):
    users: list[UserDB]
