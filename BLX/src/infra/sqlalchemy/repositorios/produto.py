from sqlalchemy.orm import Session
from src.schemas import schemas
from src.infra.sqlalchemy.models import models

""" esse script sera interface que vai conversar com o banco de dados da aplicação """

class RepositorioProduto():

    def __init__(self, db: Session) -> None:
        self.db = db 


    def criar(self, produto: schemas.Produto):
        #criar o model do banco de dados
        db_produto = models.Produto(nome=produto.nome,
                                    detalhes=produto.detalhes,
                                    preco=produto.preco,
                                    disponivel=produto.disponivel)
        #agora que o produto é um modelo ja podemos add no db e pra isso usaremos o ORM
        self.db.add(db_produto) #add o produto no banco de dados instanciado
        self.db.commit() #confirma a operação no db 
        self.db.refresh(db_produto) #atualiza o db  
        return db_produto

    def listar(self):
        produtos = self.db.query(models.Produto).all() #fazendo uma consulta a tabela produto
        return produtos
    
    def obter(self):
        pass 
    def remover(self):
        pass 