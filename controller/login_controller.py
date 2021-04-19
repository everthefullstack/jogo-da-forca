from fastapi import APIRouter, Request, Response
from pydantic import BaseModel
from model.usuario_model_schema import Usuario

class LoginModel(BaseModel):

    login: str
    senha: str

router = APIRouter()

@router.post("/login/logar_usuario")
async def logar_usuario(login: LoginModel, request: Request, response: Response):

    token = request.cookies.get("usuario")
    usuario = Usuario()

    if usuario.autenticar(token) == token and(token != 0 and token != None):
        return {"mensagem" : "usuario logado."}
    
    else:
        token, admin = usuario.logar(login.login, login.senha)
        if token:
            response.set_cookie(key="usuario", value=token)
            response.set_cookie(key="tipo", value=admin)
            return {"mensagem" : "usuario logado."}

        else:
            return {"mensagem" : "usuario não logado."}
        
@router.get("/login/deslogar_usuario")
async def deslogar_usuario(response: Response):

    try:
        response.delete_cookie(key="usuario")
        response.delete_cookie(key="tipo")
        return {"mensagem" : "usuario deslogado."}

    except:
        return {"mensagem" : "usuario não deslogado."}
