

from typing import List

from fastapi import FastAPI,Body,HTTPException, Depends
from sqlalchemy.orm import Session, session

from database.connection import get_db
from database.orm import ToDo
from database.repository import get_todo_by_todo_id, get_todos, create_todo, update_todo, delete_todo
from schema.reponse import ListToDoResponse, ToDoSchema
from schema.request import Create_Request

app = FastAPI()

@app.get("/")
def health_check_handler() :
    return {"ping":"pong"}

# 3개의 아이템을 있는 todo 데이터
todo_data ={
    1 : {
        "id" : 1,
        "contents" : "실전 api 수강0",
        "is_done" : True

    },
    2: {
        "id": 2,
        "contents": "실전 api 수강1",
        "is_done": False

    },
    3: {
        "id": 3,
        "contents": "실전 api 수강2",
        "is_done": False

    }
}
# 따로 Statuscode를 작성하지 않을 시 디폴트로 200 설정
@app.get("/todos", status_code = 200 )
def get_todos_handler(
        order : str | None = None,
        session : Session = Depends(get_db),
) -> ListToDoResponse:

    todos : List[ToDo] = get_todos(session = session)

    if order or order == "DESC" :
        return ListToDoResponse(
        todos = [ToDoSchema.model_validate(todo) for todo in todos[::-1]]
    )

    return ListToDoResponse(
        todos = [ToDoSchema.model_validate(todo) for todo in todos]
    )

@app.get("/todos/{todo_id}", status_code = 200 )
def get_todo_handler(
        todo_id:int,
        session : Session = Depends(get_db)
) -> ToDoSchema:
    todo : ToDo | None = get_todo_by_todo_id(session = session, todo_id = todo_id)

    if todo :
        return ToDoSchema.model_validate(todo)

    raise HTTPException(status_code = 404,detail = "Todo Not Found")


@app.post("/todos",status_code = 201)
def create_todo_handler(
        request : Create_Request,
        session : Session = Depends(get_db),
) -> ToDoSchema :
    todo: ToDo = ToDo.create(request= request)
    todo: ToDo = create_todo(session = session, todo=todo) # id = int

    return ToDoSchema.model_validate(todo)

@app.patch("/todos/{todo_id}",status_code= 200)
def update_todo_handler(
        todo_id : int,
        is_done : bool  = Body(..., embed=True),

) :
    todo = todo_data.get(todo_id)
    if todo :
        # update
        if is_done is True :
            todo.done()
        else :
            todo.undone()

        todo : ToDo = update_todo(Session=session, todo = todo)

        return ToDoSchema.model_validate(todo)

    raise HTTPException(status_code=404,detail="Todo Not Found")

@app.delete("/todos{todo_id}",status_code=204)
def delete_todo_handler(
        todo_id : int,
        session : Session = Depends(get_db),
) :
    todo: ToDo | None = get_todo_by_todo_id(session=session, todo_id=todo_id)

    if not todo:
        #delete
        raise HTTPException(status_code=404, detail="Todo Not Found")
    delete_todo(session= session, todo_id = todo_id)


