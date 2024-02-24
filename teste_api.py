from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get('/saudacao/{nome}')
def root(nome: str):
    text = f' ola, {nome}, seja bem-vinda(o)'
    return {"mensagem": text}

@app.get('/dobro')
def dobro(numero: int = 10):
    resultado = numero * 2
    mensage_resultado = f"o dobro de {numero} é {resultado}"
    return {"resultado": mensage_resultado }

class Produto(BaseModel):
    nome: str
    preco: float


@app.post('/produtos')
def produto(produto: Produto):
    return { "mensagem": f'Produto {produto.nome} R${produto.preco} cadastrado com sucesso!'}


class Animal(BaseModel):
    id: int 
    nome: str 
    idade: int 
    sexo: str
    cor: str 

lista_animais = []

@app.post('/animais')
def cadastrar_animal(animal: Animal):
    lista_animais.append({"nome": animal.nome, "idade": animal.idade, "sexo": animal.sexo, "cor": animal.cor}) 
    return lista_animais

@app.get('/animais')
def animais_cadastrados():
    return lista_animais




#@app.delete('/animais/{id}')
