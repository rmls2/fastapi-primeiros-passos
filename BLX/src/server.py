from fastapi import FastAPI, Depends #vai servir pra fazer a conexão com o banco de dados
from sqlalchemy.orm import Session
from src.schemas.schemas import Produto
from src.infra.sqlalchemy.config.database import get_bd, criar_bd
from src.infra.sqlalchemy.repositorios.produto import RepositorioProduto

criar_bd()

app = FastAPI()

@app.post('/produtos')
def criar_produtos(produto: Produto, db: Session = Depends(get_bd)):
    produto_criado = RepositorioProduto(db).criar(produto)
    return produto_criado


@app.get('/produtos')
def listar_produtos(db: Session = Depends(get_bd)):
    produtos = RepositorioProduto(db).listar()
    return produtos