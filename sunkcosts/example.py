from rich.console import Console
from datetime import datetime
from attr import field
from pydantic import BaseModel, field_validator


class User(BaseModel):
    username: str
    email: str

    # @field("email")


class RedditComment(BaseModel):
    date_posted: datetime
    is_edited: bool
    parent_user: User


com = {
    "date_posted": "2022-01-01 00:00:00",
    "is_edited": False,
    "parent_user": {"username": "hart", "email": "hart@gmail.com"},
}

pycom = RedditComment.model_validate(com)


Console().print(pycom)
