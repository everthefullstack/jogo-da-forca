from fastapi import APIRouter, Request
from pydantic import BaseModel
from model.palavra_model_schema import PalavraModel

class Palavra(BaseModel):

    nome: str
    fkcodcategoria: int

router = APIRouter()

@router.post("/admin/cadastrar_palavra")
async def create_palavra(palavra: Palavra, request: Request):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        palavra = PalavraModel(nome = palavra.nome, fkcodcategoria = palavra.fkcodcategoria)
        if palavra.create_palavra():
            return {"mensagem" : "palavra cadastrada."}
        
        else:
            return {"mensagem" : "palavra não cadastrada."}
    
    else:
        return {"mensagem" : "Somente um ADM pode criar uma palavra."}

@router.get("/admin/ler_palavras")
async def read_palavras(request: Request):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        lista_palavras = []
        palavras = PalavraModel.read_palavras()

        if palavras:

            for palavra in palavras:
                lista_palavras.append(palavra.json())

            return {'mensagem': lista_palavras}
   
        return {"mensagem" : lista_palavras}

    else:
        return {"mensagem" : "Somente um ADM pode solicitar a lista de palavras."}

@router.get("/admin/ler_palavras/{idpalavra}")
async def read_palavra(request: Request, idpalavra: int):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        palavra = PalavraModel.read_palavra(idpalavra)

        if palavra:
            return {'mensagem': palavra.json()}

        else:
            return {"mensagem" : "palavra não cadastrada."}

    else:
        return {"mensagem" : "Somente um ADM pode solicitar uma palavra."}

@router.put("/admin/editar_palavra/{idpalavra}")
async def edit_palavra(idpalavra: int, palavra: Palavra, request: Request):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        pal = PalavraModel.read_palavra(idpalavra)

        if pal:
            pal.update_palavra(nome = palavra.nome, fkcodcategoria = palavra.fkcodcategoria)
            return {"mensagem" : "palavra editada."}

        else:
            return {"mensagem" : "palavra não editada."}

    else:
        return {"mensagem" : "Somente um ADM pode editar uma palavra."}

@router.delete("/admin/deletar_palavra/{idpalavra}")
async def delete_palavra(idpalavra: int, request: Request):

    tipo = bool(request.headers["tipo"])
    if tipo == True:

        palavra = PalavraModel.read_palavra(idpalavra)

        if palavra:
            palavra.delete_palavra()
            return {"mensagem" : "palavra deletada."}

        else:
            return {"mensagem" : "palavra não deletada."}

    else:
        return {"mensagem" : "Somente um ADM pode deletar uma palavra."}
