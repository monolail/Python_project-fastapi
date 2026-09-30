from fastapi import FastAPI

from api import todo,user
app = FastAPI()
app.include_router(todo.router)
app.include_router(user.router)
app.include_router(todo.router)
@app.get("/")
def health_check_handler() :
    return {"ping":"pong"}




# 따로 Statuscode를 작성하지 않을 시 디폴트로 200 설정


