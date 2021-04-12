from fastapi import FastAPI, APIRouter
from controller import login_controller, cadastro_controller, cria_banco_controller

app = FastAPI()

app.include_router(login_controller.router)
app.include_router(cadastro_controller.router)
app.include_router(cria_banco_controller.router)

@app.get("/")
def root():
    
    return {"message": "Hello Bigger Applications!"}

#uvicorn app:app --reload