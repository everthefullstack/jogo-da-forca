from fastapi import APIRouter, Request
from pydantic import BaseModel
from model.usuario_model_schema import Usuario

router = APIRouter()

@router.get("/ranking/mostrar_ranking")
async def read_ranking(request: Request):

    token = request.cookies.get("usuario")
    usuario = Usuario()

    if usuario.autenticar(token) == token and(token != 0 and token != None):

        lista_usuarios = []
        usuarios = usuario.read_usuarios()

        if usuarios:

            for usuario in usuarios:
                lista_usuarios.append(usuario.json())

            return {'message': lista_usuarios}
   
        return {"mensagem" : "usuarios não cadastrados."}
    
    else:
        return {"mensagem" : "Não foi possível mostrar o ranking."}