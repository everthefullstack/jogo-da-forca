from fastapi import APIRouter, Request
from pydantic import BaseModel
from model.usuario_model_schema import Usuario
from model.compra_model_schema import CompraModel
from model.shop_model_schema import ShopModel

class Compra(BaseModel):

    fkcodshop: int
    fkcodusuario: int
    quantidade: int

class CompraUsuario(BaseModel):

    fkcodusuario: int

router = APIRouter()

@router.post("/compra/comprar_skin")
async def create_compra(compra: Compra, request: Request):

    token = request.headers["usuario"]
    usuario = Usuario()

    if usuario.autenticar(token) == token and(token != 0 and token != None):
        
        cmp = CompraModel(fkcodshop = compra.fkcodshop, fkcodusuario = compra.fkcodusuario, quantidade = compra.quantidade)
        shop = ShopModel.read_shop(idshop=compra.fkcodshop)
        usuario = Usuario.read_usuario(idusuario=compra.fkcodusuario)

        if usuario and shop:
            
            if usuario.pontuacao < (shop.valor * compra.quantidade):
                return {"mensagem" : "Usuário não tem pontos suficientes para compra."}

            else:
                cmp.create_compra(compra.fkcodshop, compra.fkcodusuario, compra.quantidade)
                usuario.pontuacao = usuario.pontuacao - (shop.valor * compra.quantidade)
                usuario.save()
                return {"mensagem" : usuario.read_usuario(idusuario = compra.fkcodusuario).json()}
        else:
            return {"mensagem" : "Usuário ou Shop inexistente."}

    else:
        return {"mensagem" : "Usuário não autenticado."}

@router.get("/compra/ler_compras")
async def read_compras(compra_usuario: CompraUsuario, request: Request):

    token = request.headers["usuario"]
    usuario = Usuario()
    lista_cmp = []

    if usuario.autenticar(token) == token and(token != 0 and token != None):
        
        cmp = CompraModel.read_compras_usuario(compra_usuario.fkcodusuario)

        if cmp:

            for compra in cmp:
                lista_cmp.append(compra.json())

            return {"mensagem" : lista_cmp}

        else:
            return {"mensagem" : lista_cmp}

    else:
        return {"mensagem" : "Usuário não autenticado."}
    
@router.get("/compra/ler_compras")
async def read_compras(compra_usuario: CompraUsuario, request: Request):

    token = request.headers["usuario"]
    usuario = Usuario()
    lista_cmp = []

    if usuario.autenticar(token) == token and(token != 0 and token != None):
        
        cmp = CompraModel.read_compras_usuario(compra_usuario.fkcodusuario)

        if cmp:

            for compra in cmp:
                lista_cmp.append(compra.json())

            return {"mensagem" : lista_cmp}

        else:
            return {"mensagem" : lista_cmp}

    else:
        return {"mensagem" : "Usuário não autenticado."}
    
