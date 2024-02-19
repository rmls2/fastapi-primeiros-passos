from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional #usada para tipar objetos e variáveis 
from uuid import uuid4
from fastapi.middleware.cors import CORSMiddleware #add middleware

app = FastAPI()

origins = ['http://127.0.0.1:5500']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class Animal(BaseModel):

    id: int | None = None
    nome: str 
    idade: int 
    sexo: str
    cor: str 

bd: List[Animal] = []  #tipamos nossa lista bd que só receberá objeto da classe Animal 

@app.post('/animais')
def cadastrar_animal(animal: Animal):
   animal.id = str(uuid4())
   bd.append(animal)
   return None

@app.get('/animais')
def animais_cadastrados():
    return bd

@app.get('/animais/{id}')
def retorna_animal_id(id: str):
    for animal in bd: 
        if animal.id == id:
            return animal
    return {"erro": "animal não encontrado"}

@app.delete('/animais/{id_procurado}')
def remove_animal(id_procurado: str):
    posicao = -1
    for index,animal in enumerate(bd):
        if animal.id == id_procurado:
            posicao = index
            break
    if posicao != -1:
        bd.pop(posicao)
        return {"mensagem": "animal removido com suceso"}
    else:
        return {"mensagem": "animal não localizado"}
    