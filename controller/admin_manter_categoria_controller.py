from fastapi import APIRouter, Request
from pydantic import BaseModel
from model.categoria_model_schema import CategoriaModel

class Categoria(BaseModel):

    nome: str

router = APIRouter()

@router.post("/admin/cadastrar_categoria")
async def create_categoria(categoria: Categoria, request: Request):

    tipo = request.headers["tipo"]
    if tipo.lower() == "true" or tipo.lower() == "1":

        categoria = CategoriaModel(nome = categoria.nome)

        if categoria.create_categoria():
            return {"mensagem" : "categoria cadastrada."}
        
        else:
            return {"mensagem" : "categoria não cadastrada."}
    
    else:
        return {"mensagem" : "Somente um ADM pode criar uma categoria."}

@router.get("/admin/ler_categorias")
async def read_categorias(request: Request):

    tipo = request.headers["tipo"]
    if tipo.lower() == "true" or tipo.lower() == "1":

        lista_categorias = []
        categorias = CategoriaModel.read_categorias()

        if categorias:

            for categoria in categorias:
                lista_categorias.append(categoria.json())

            return {'mensagem': lista_categorias}
   
        return {"mensagem" : lista_categorias}

    else:
        return {"mensagem" : "Somente um ADM pode solicitar a lista de categorias."}

@router.get("/admin/ler_categorias/{idcategoria}")
async def read_categoria(request: Request, idcategoria: int):

    tipo = request.headers["tipo"]
    if tipo.lower() == "true" or tipo.lower() == "1":

        categoria = CategoriaModel.read_categoria(idcategoria)

        if categoria:
            return {'mensagem': categoria.json()}

        else:
            return {"mensagem" : "categoria não cadastrada."}

    else:
        return {"mensagem" : "Somente um ADM pode solicitar uma categoria."}

@router.put("/admin/editar_categoria/{idcategoria}")
async def edit_categoria(idcategoria: int, categoria: Categoria, request: Request):

    tipo = request.headers["tipo"]
    if tipo.lower() == "true" or tipo.lower() == "1":

        cat = CategoriaModel.read_categoria(idcategoria)
        if cat:
            if cat.update_categoria(nome = categoria.nome):
                return {"mensagem" : "categoria editada."}
            
            else:
                return {"mensagem" : "categoria não editada."}

        else:
            return {"mensagem" : "categoria não editada."}

    else:
        return {"mensagem" : "Somente um ADM pode editar uma categoria."}

@router.delete("/admin/deletar_categoria/{idcategoria}")
async def delete_categoria(idcategoria: int, request: Request):

    tipo = request.headers["tipo"]
    if tipo.lower() == "true" or tipo.lower() == "1":

        categoria = CategoriaModel.read_categoria(idcategoria)

        if categoria:
            categoria.delete_categoria()
            return {"mensagem" : "categoria deletada."}

        else:
            return {"mensagem" : "categoria não deletada."}

    else:
        return {"mensagem" : "Somente um ADM pode deletar uma categoria."}
