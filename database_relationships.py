from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import SQLAlchemyError

Base = declarative_base()


class structure_database_relationships(Base):
    __tablename__ = 'Relationships'

    id = Column(Integer, primary_key=True, autoincrement=True)
    relation_id = Column(Integer)
    partner_iln = Column(String)
    partner_name = Column(String)
    direction = Column(String)
    document_type = Column(String)
    document_version = Column(String)
    document_standard = Column(String)
    document_test = Column(String)
    description = Column(String)
    test = Column(String)


class session_relationships:

    def __init__(self, url):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def select_data_relationships(self, relation_id_value, partner_iln_value, partner_name_value, direction_value, document_type_value, document_version_value, document_standard_value, document_test_value, description_value, test_value):
        fop = structure_database_relationships(relation_id=relation_id_value, partner_iln=partner_iln_value, partner_name=partner_name_value, direction=direction_value,
                        document_type=document_type_value, document_version=document_version_value, document_standard=document_standard_value, document_test=document_test_value,
                        description=description_value, test=test_value)
        try:
            self.session.add(fop)
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()

    def update_table_relationships(self, relation_id_update, partner_iln_update, partner_name_update, direction_update, document_type_update, document_version_update, document_standard_update, document_test_update, description_update, test_update):
        try:
            update_relationships = self.session.query(structure_database_relationships).order_by(structure_database_relationships.direction).update({
                structure_database_relationships.relation_id: relation_id_update,
                structure_database_relationships.partner_iln: partner_iln_update,
                structure_database_relationships.partner_name: partner_name_update,
                structure_database_relationships.direction: direction_update,
                structure_database_relationships.document_type: document_type_update,
                structure_database_relationships.document_version: document_version_update,
                structure_database_relationships.document_standard: document_standard_update,
                structure_database_relationships.document_test: document_test_update,
                structure_database_relationships.description: description_update,
                structure_database_relationships.test: test_update
            })
            self.session.commit()
        except SQLAlchemyError:
            self.session.rollback()


if __name__ == "__main__":
    db = session_relationships("sqlite:///request_of_methods.db")