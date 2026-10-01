from pydantic import BaseModel, ConfigDict

class ToDoSchema(BaseModel) :
    id : int
    contents : str
    is_done : bool

    class Config :
        orm_mode = True


class ListToDoResponse(BaseModel) :
    todos : list[ToDoSchema]

class UserSchema(BaseModel) :
    id:int
    username :str
    class Config :
        orm_mode = True
