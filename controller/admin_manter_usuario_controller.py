from fastapi import APIRouter, Request
from pydantic import BaseModel
from model.usuario_model_schema import Admin

class Cadastro(BaseModel):

    login: str
    senha: str
    admin: bool

router = APIRouter()

@router.post("/admin/cadastrar_usuario")
async def create_usuario(cadastro: Cadastro, request: Request):

    tipo = bool(request.cookies.get("tipo"))
    if tipo == True:

        usuario = Admin(login = cadastro.login, senha = cadastro.senha, admin = cadastro.admin)

        if usuario.create_usuario():
            return {"mensagem" : "usuario cadastrado."}
        
        else:
            return {"mensagem" : "usuario não cadastrado."}
    
    else:
        return {"mensagem" : "Somente um ADM pode criar um usuário."}

@router.get("/admin/ler_usuarios")
async def read_usuarios(request: Request):

    tipo = bool(request.cookies.get("tipo"))

    if tipo == True:

        lista_usuarios = []
        usuarios = Admin.read_usuarios()

        if usuarios:

            for usuario in usuarios:
                lista_usuarios.append(usuario.json())

            return {'message': lista_usuarios}
   
        return {"mensagem" : "usuarios não cadastrados."}

    else:
        return {"mensagem" : "Somente um ADM pode solicitar a lista de usuários."}

@router.get("/admin/ler_usuarios/{idusuario}")
async def read_usuario(request: Request, idusuario: int):

    tipo = bool(request.cookies.get("tipo"))

    if tipo == True:

        usuario = Admin.read_usuario(idusuario)

        if usuario:
            return {'message': usuario.json()}

        else:
            return {"mensagem" : "usuario não cadastrado."}

    else:
        return {"mensagem" : "Somente um ADM pode solicitar um usuario."}

@router.put("/admin/editar_usuario/{idusuario}")
async def edit_usuario(idusuario: int, cadastro: Cadastro, request: Request):

    tipo = bool(request.cookies.get("tipo"))

    if tipo == True:

        usuario = Admin.read_usuario(idusuario)

        if usuario:
            usuario.update_usuario(login = cadastro.login, senha = cadastro.senha, admin = cadastro.admin)
            return {"mensagem" : "usuario editado."}

        else:
            return {"mensagem" : "usuario não editado."}

    else:
        return {"mensagem" : "Somente um ADM pode editar um usuario."}

@router.delete("/admin/deletar_usuario/{idusuario}")
async def delete_usuario(idusuario: int, request: Request):

    tipo = bool(request.cookies.get("tipo"))

    if tipo == True:

        usuario = Admin.read_usuario(idusuario)

        if usuario:
            usuario.delete_usuario()
            return {"mensagem" : "usuario deletado."}

        else:
            return {"mensagem" : "usuario não deletado."}

    else:
        return {"mensagem" : "Somente um ADM pode deletar um usuario."}
