from typing import List

from sqlalchemy import select
from sqlalchemy.orm import Session

from database.orm import ToDo


# 레포지토리 패턴
def get_todos(session:Session) -> List[ToDo] :
    return list(session.scalars(select(ToDo)))