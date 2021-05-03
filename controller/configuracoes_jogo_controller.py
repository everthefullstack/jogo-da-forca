from fastapi import APIRouter, Request
from pydantic import BaseModel
from model.usuario_model_schema import Usuario
from model.compra_model_schema import CompraModel
from model.palavra_model_schema import PalavraModel
from model.categoria_model_schema import CategoriaModel
router = APIRouter()

class Configuracao(BaseModel):
    fkcodusuario: int

@router.post("/configuracao/ler_configuracoes")
async def read_configuracoes(configuracao: Configuracao, request: Request):

    token = request.headers["usuario"]
    usuario = Usuario()

    if usuario.autenticar(token) == token and(token != 0 and token != None):

        lista_config = []
        lista_cmp = []
        lista_plv = []
        lista_cat = []

        cmp = CompraModel.read_compras_usuario(fkcodusuario=configuracao.fkcodusuario)
        plv = PalavraModel.read_palavras()
        cat = CategoriaModel.read_categorias()
        
        if cmp:

            for compra in cmp:
                lista_cmp.append(compra.json())

        if plv:
            for palavra in plv:
                lista_plv.append(palavra.json())
        
        if cat:
            for categoria in cat:
                lista_cat.append(categoria.json())
        
        lista_config.append({"lista_compras": lista_cmp})
        lista_config.append({"lista_palavras": lista_plv})
        lista_config.append({"lista_categorias": lista_cat})

        return {"mensagem" : lista_config}

    else:
        return {"mensagem" : "Usuário não autenticado."}