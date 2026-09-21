from sqlalchemy import Boolean, Column,Integer,String
from sqlalchemy.orm import declarative_base

from schema.request import Create_Request

Base = declarative_base()


class ToDo(Base) :
    __tablename__ = "todo"

    id = Column(Integer, primary_key= True, index = True)
    contents = Column(String(256), nullable = False)
    is_done = Column(Boolean, nullable = False)

    def __rep__(self):
        return f"ToDo(id={self.id}, contents={self.contents}, is_done={self.is_done}"

    @classmethod
    def create(cls , request : Create_Request):
        return cls(
            contents = request.contents,
            is_done = request.id_done,
        )

    def done(self) :
        self.is_done = True
        return self

    def undone(self) -> "ToDo" :
        self.is_done = False
        return self
