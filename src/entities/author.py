from dataclasses import dataclass
from datetime import datetime


@dataclass
class Author:
    id: int
    name: str
    created_at: datetime = datetime.now()
