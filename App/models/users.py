from pydantic import BaseModel


class Users(BaseModel):
    user: str = None

