from pydantic import BaseModel


class Create_Request(BaseModel) :
    content : str
    is_done : bool


