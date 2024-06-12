from datetime import datetime
from pydantic import BaseModel


class Message(BaseModel):
    user_id: int
    dialog: str
    text: str
    datetime: datetime
