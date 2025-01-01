from dataclasses import dataclass
from datetime import datetime
from typing import Optional


@dataclass
class Author:
    name: str
    id: Optional[int] = None
    created_at: datetime = datetime.now()
