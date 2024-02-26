from sqlalchemy import Column, Integer, String, Boolean, Float
from src.infra.sqlalchemy.config.database import Base

""" A classe  models.py representa dados da aplicação """

class Produto(Base):
    __tablename__ = 'produto'

    id = Column(Integer, primary_key = True, index = True)
    nome = Column(String)
    detalhes = Column(String)
    preco = Column(Float)
    disponivel = Column(Boolean)