from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class database(Base):
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


class session_relationships(database):
    def __init__(self, url):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def create_table_relationships(self):
        fop = database(relation_id=12432, partner_iln="test", partner_name="test", direction="test",
                       document_type="test", document_version="test", document_standard="test", document_test="test",
                       description="test", test="test")
        self.session.add(fop)
        self.session.commit()

    def update_table_relationships(self, relation_id_update, partner_iln_update, partner_name_update, direction_update, document_type_update, document_version_update, document_standard_update, document_test_update, description_update, test_update):
        update_relationships = self.session.query(database).filter_by(direction="IN").one()
        update_relationships.relation_id = relation_id_update
        update_relationships.partner_iln = partner_iln_update
        update_relationships.partner_name = partner_name_update
        update_relationships.direction = direction_update
        update_relationships.document_type = document_type_update
        update_relationships.document_version = document_version_update
        update_relationships.document_standard = document_standard_update
        update_relationships.document_test = document_test_update
        update_relationships.description = description_update
        update_relationships.test = test_update
        self.session.add(update_relationships)
        self.session.commit()


if __name__ == "__main__":
    db = session_relationships("sqlite:///request_of_methods.db")
