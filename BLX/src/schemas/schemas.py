from pydantic import BaseModel
from typing import List

# pedido = NewType('pedido', Pedido)

class Usuario(BaseModel):
    id: str | None = None
    nome: str
    telefone: str


class Produto(BaseModel):
    id: str | None = None
    nome: str
    detalhes: str
    preco: float
    disponivel: bool = False

    class config:
        orm_mode = True    #é para que a partir de um modelo criar uma schema

class Pedido(BaseModel):
    id: str | None = None
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: str | None = 'sem observaçoes'
