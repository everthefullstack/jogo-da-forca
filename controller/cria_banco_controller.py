from fastapi import APIRouter
from model.usuario_model_schema import UsuarioModel
from model.categoria_model_schema import CategoriaModel
from model.palavra_model_schema import PalavraModel
from model.shop_model_schema import ShopModel
from model.compra_model_schema import CompraModel

router = APIRouter()

@router.get("/criar_banco")
def cria_banco():

    try:
        UsuarioModel.create_table()
        CategoriaModel.create_table()
        PalavraModel.create_table()
        ShopModel.create_table()
        CompraModel.create_table()
        return {"Hello": "banco criado"}

    except:
        return {"Erro": "Banco não criado"}
