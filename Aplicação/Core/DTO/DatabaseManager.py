# 🔹 Classe genérica para gerenciar o banco (serve para qualquer dto_obj)
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

class DatabaseManager:
    def __init__(self, db_url):
        self.engine = create_engine(db_url)
        self.Session = sessionmaker(bind=self.engine)
        Base.metadata.create_all(self.engine)  # Cria tabelas se necessário

    def get_session(self):
        """Retorna uma nova sessão do banco."""
        return self.Session()

# 🔹 Repositório genérico para qualquer tabela
class GenericRepository:
    def __init__(self, session, dto_obj):
        self.session = session
        self.dto_obj = dto_obj

    def get(self, item_id):
        """Busca um item pelo ID."""
        return self.session.get(self.dto_obj, item_id)

    def save(self, item):
        """Salva o item no banco se ainda não existir. Se já existir, mescla para evitar conflitos."""
        item = self.session.merge(item)
        self.session.add(item)
        self.session.commit()

    def get_all(self):
        """Retorna todos os registros da tabela."""
        return self.session.query(self.dto_obj).all()