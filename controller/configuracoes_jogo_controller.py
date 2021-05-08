from fastapi import APIRouter, Request
from pydantic import BaseModel
from model.usuario_model_schema import Usuario
from model.compra_model_schema import CompraModel
from model.palavra_model_schema import PalavraModel
from model.categoria_model_schema import CategoriaModel

router = APIRouter()

class Configuracao(BaseModel):
    fkcodusuario: int

class Categoria(BaseModel):
    fkcodcategoria: int

class Compra(BaseModel):
    idcompra: int

class Pontuacao(BaseModel):
    pontuacao: float

@router.post("/configuracao/ler_configuracoes")
async def read_configuracoes(configuracao: Configuracao, request: Request):

    token = request.headers["usuario"]
    usuario = Usuario()

    if usuario.autenticar(token) == token and(token != 0 and token != None):

        lista_config = []
        lista_cmp = []
        lista_cat = []

        cmp = CompraModel.read_compras_usuario(fkcodusuario=configuracao.fkcodusuario)
        cat = CategoriaModel.read_categorias()
        
        if cmp:

            for compra in cmp:
                lista_cmp.append(compra.json())
        
        if cat:
            for categoria in cat:
                lista_cat.append(categoria.json())
        
        lista_config.append({"lista_compras": lista_cmp})
        lista_config.append({"lista_categorias": lista_cat})

        return {"mensagem" : lista_config}

    else:
        return {"mensagem" : "Usuário não autenticado."}

@router.post("/configuracao/ler_palavras_categoria")
async def read_palavras_categoria(categoria: Categoria, request: Request):

    token = request.headers["usuario"]
    usuario = Usuario()

    if usuario.autenticar(token) == token and(token != 0 and token != None):

        lista_plv = []

        if categoria.fkcodcategoria == 0:

            plv = PalavraModel.read_palavras()

            if plv:
                for palavra in plv:
                    lista_plv.append(palavra.json())

        else:

            plv = PalavraModel.read_palavras_por_categoria(fkcodcategoria=categoria.fkcodcategoria)

            if plv:
                for palavra in plv:
                    lista_plv.append(palavra.json())

        return {"mensagem" : lista_plv}

    else:

        return {"mensagem" : "Usuário não autenticado."}

@router.post("/configuracao/altera_quantidade")
async def update_quantidade(comprausuario: Compra, request: Request):

    token = request.headers["usuario"]
    usuario = Usuario()

    if usuario.autenticar(token) == token and(token != 0 and token != None):

        compra = Compra.read_compra(idcompra=comprausuario.idcompra)
        
        if compra.update_compra():
            return {"mensagem" : compra.json()}

        else:
            return {"mensagem" : "Quantidade não alterada."}
    else:
        return {"mensagem" : "Usuário não autenticado."}

@router.post("/configuracao/salvar_pontuacao")
async def update_pontuacao(pontuacao: Pontuacao, request: Request):

    token = request.headers["usuario"]
    usuario = Usuario()

    if usuario.autenticar(token) == token and(token != 0 and token != None):

        if usuario.update_pontuacao(pontuacao.pontuacao):
            return {"mensagem" : usuario.json()}

        else:
            return {"mensagem" : "Pontuações não alteradas."}
    else:
        return {"mensagem" : "Usuário não autenticado."}