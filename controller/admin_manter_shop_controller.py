from fastapi import APIRouter, Request
from pydantic import BaseModel
from model.shop_model_schema import ShopModel

class Shop(BaseModel):

    nome: str
    valor: str
    imagem: str

router = APIRouter()

@router.post("/admin/cadastrar_shop")
async def create_shop(shop: Shop, request: Request):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        shop = ShopModel(nome = shop.nome, valor = shop.valor, imagem = shop.imagem)
        if shop.create_shop():
            return {"mensagem" : "shop cadastrado."}
        
        else:
            return {"mensagem" : "shop não cadastrado."}
    
    else:
        return {"mensagem" : "Somente um ADM pode criar um shop."}

@router.get("/admin/ler_shops")
async def read_shops(request: Request):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        lista_shops = []
        shops = ShopModel.read_shops()

        if shops:

            for shop in shops:
                lista_shops.append(shop.json())

            return {'mensagem': lista_shops}
   
        return {"mensagem" : lista_shops}

    else:
        return {"mensagem" : "Somente um ADM pode solicitar a lista de shops."}

@router.get("/admin/ler_shops/{idshop}")
async def read_shop(request: Request, idshop: int):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        shop = ShopModel.read_shop(idshop)

        if shop:
            return {'mensagem': shop.json()}

        else:
            return {"mensagem" : "shop não cadastrada."}

    else:
        return {"mensagem" : "Somente um ADM pode solicitar uma shop."}

@router.put("/admin/editar_shop/{idshop}")
async def edit_shop(idshop: int, shop: Shop, request: Request):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        sho = ShopModel.read_shop(idshop)

        if sho:
            sho.update_shop(nome = shop.nome, valor = shop.valor, imagem = shop.imagem)
            return {"mensagem" : "shop editada."}

        else:
            return {"mensagem" : "shop não editada."}

    else:
        return {"mensagem" : "Somente um ADM pode editar uma shop."}

@router.delete("/admin/deletar_shop/{idshop}")
async def delete_shop(idshop: int, request: Request):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        shop = ShopModel.read_shop(idshop)

        if shop:
            shop.delete_shop()
            return {"mensagem" : "shop deletada."}

        else:
            return {"mensagem" : "shop não deletada."}

    else:
        return {"mensagem" : "Somente um ADM pode deletar uma shop."}
      