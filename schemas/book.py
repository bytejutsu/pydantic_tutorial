from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel


class Book(BaseModel):
    id: str
    title: str
    subtitle: str
    author: str

