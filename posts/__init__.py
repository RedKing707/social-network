from pydantic import BaseModel
from datetime import datetime


class PublicPostValidator(BaseModel):
    user_id: int
    post_text: str
    publish_date: datetime


class EditPostValidator(BaseModel):
    post_id: int
    new_text: str
    user_id: int
