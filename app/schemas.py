from pydantic import BaseModel


class User(BaseModel):
    email: str
    password: str


class NewUser(User):
    role: str
