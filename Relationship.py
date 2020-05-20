from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Relationship(Base):
    __tablename__ = 'Relationships'

    relation_id = Column(Integer, primary_key=True)
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
