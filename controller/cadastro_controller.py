from fastapi import APIRouter
from pydantic import BaseModel
from model.usuario_model_schema import Usuario

class CadastroModel(BaseModel):

    login: str
    senha: str

router = APIRouter()

@router.post("/cadastro/cadastrar_usuario/")
async def create_usuario(cadastro: CadastroModel):

    usuario = Usuario(login = cadastro.login, senha = cadastro.senha)

    if usuario.create_usuario():
        return {"mensagem" : "usuario cadastrado."}
    
    else:
        return {"mensagem" : "usuario não cadastrado."}
