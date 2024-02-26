from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./app_blx.db"
# SQLALCHEMY_DATABASE_URL = "postgresql://postgres:Unic0rn1o#@local/db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #faz a conexão com o banco de dados 

Base = declarative_base() #instancia a classe base que vai ficar herdando os nossos modelos

def criar_bd():
    Base.metadata.create_all(bind=engine)

# como vamos disponibilizar conexões com a aplicação principal
    
def get_bd():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()