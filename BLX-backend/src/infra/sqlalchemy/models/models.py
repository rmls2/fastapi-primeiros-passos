from sqlalchemy import column, Integer, String, Boolean, Float
from src.infra.sqlalchemy.config.database import Base


class Produto():
    __tablename__ = 'produto'

    id = column(Integer, primary_key = True, index = True)
    nome = column(String)
    detalhes = column(String)
    preco = column(Float)
    disponivel = column(Boolean)