# 🔹 Classe genérica para gerenciar o banco (serve para qualquer dto_class)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine
import pymongo

Base = declarative_base()

class DatabaseManager:
    def __init__(self, db_url, mongo_url = None):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine, autoflush=False)
        Base.metadata.create_all(self.engine)  # Cria tabelas se necessário
        if mongo_url is not None:
            self.mongo_client = pymongo.MongoClient("mongodb://localhost:27017/")

    def get_session(self):
        """Retorna uma nova sessão do banco."""
        return self.Session()
    
    def get_mongo_db(self):
        return self.mongo_client["mydb"]

# 🔹 Repositório genérico para qualquer tabela
class GenericRepository:
    def __init__(self, session, dto_class):
        self.session = session
        self.dto_class = dto_class        

    def get(self, item_id):
        """Busca um item pelo ID."""
        return self.session.get(self.dto_class, item_id)
    
    def filter_by(self, filters):
        """Busca um item pelo ID."""
        return self.session.query(self.dto_class).filter_by(**filters) 

    def save(self, item):
        self.session.add(item)
        self.session.commit()

    def get_all(self):
        """Retorna todos os registros da tabela."""
        return self.session.query(self.dto_class).all()