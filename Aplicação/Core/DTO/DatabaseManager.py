# 🔹 Classe genérica para gerenciar o banco (serve para qualquer ModelDTOo)
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
    def __init__(self, session, ModelDTO):
        self.session = session
        self.ModelDTO = ModelDTO

    def get(self, item_id):
        """Busca um item pelo ID."""
        return self.session.get(self.ModelDTO, item_id)

    def save(self, item):
        """Salva ou atualiza um item no banco."""
        self.session.add(item)
        self.session.commit()

    def get_all(self):
        """Retorna todos os registros da tabela."""
        return self.session.query(self.ModelDTO).all()