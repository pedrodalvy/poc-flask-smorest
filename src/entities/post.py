from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Post:
    title: str
    content: str
    author_id: int
    id: Optional[int] = None
    created_at: datetime = datetime.now()
