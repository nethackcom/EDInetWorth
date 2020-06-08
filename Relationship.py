from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine


Base = declarative_base()

# URL базы данных
__url = "sqlite:///request_of_methods.db"

class Relationship(Base):
    __tablename__ = 'Relationships'

    relation_id = Column(Integer, primary_key=True, autoincrement=True, nullable=False, unique=True)
    partner_iln = Column(String)
    partner_name = Column(String)
    direction = Column(String)
    document_type = Column(String)
    document_version = Column(String)
    document_standard = Column(String)
    document_test = Column(String)
    description = Column(String)
    test = Column(String)
    form = Column(String)

    def __init__(self, relation_id, partner_iln, partner_name, direction, document_type, document_version, document_standard, document_test, description, test, form):
        self.relation_id = relation_id
        self.partner_iln = partner_iln
        self.partner_name = partner_name
        self.direction = direction
        self.document_type = document_type
        self.document_version = document_version
        self.document_standard = document_standard
        self.document_test = document_test
        self.description = description
        self.test = test
        self.form = form


# Создаем нашу БД
engine = create_engine(__url)

# Создаем нашу таблицу
Base.metadata.create_all(engine)