from pydantic import BaseModel
from typing import List

# pedido = NewType('pedido', Pedido)

class Usuario(BaseModel):
    id: str | None = None
    nome: str
    telefone: str
    minhas_vendas: List[Pedido]
    meus_produtos: List[Produto]
    meus_pedidos: List[Pedido]


class Produto(BaseModel):
    id: str | None = None
    nome: str
    # usuario: Usuario
    detalhes: str
    preco: float
    disponivel: bool = False

class Pedido(BaseModel):
    id: str | None = None
    usuario: Usuario
    Produto: Produto
    quantidade: int
    entrega: bool = True
    endereco: str
    observacoes: str | None = 'sem observaçoes'
