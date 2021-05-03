from fastapi import FastAPI, APIRouter
from fastapi.middleware.cors import CORSMiddleware
from controller import (login_controller, cadastro_controller, cria_banco_controller, admin_manter_usuario_controller, 
                        admin_manter_categoria_controller, admin_manter_palavra_controller, ranking_controller, 
                        admin_manter_shop_controller, compra_shop_controller)

app = FastAPI()

app.include_router(login_controller.router)
app.include_router(cadastro_controller.router)
app.include_router(cria_banco_controller.router)
app.include_router(admin_manter_usuario_controller.router)
app.include_router(admin_manter_categoria_controller.router)
app.include_router(admin_manter_palavra_controller.router)
app.include_router(ranking_controller.router)
app.include_router(admin_manter_shop_controller.router)
app.include_router(compra_shop_controller.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    
    return {"message": "Hello Bigger Applications!"}

#uvicorn app:app --reload