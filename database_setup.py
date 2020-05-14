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

    def update_table_relationships(self):
        update_relationships = self.session.query(database).filter_by(direction="IN").one()
        update_relationships.relation_id = 1
        update_relationships.partner_iln = "content"
        update_relationships.partner_name = "content"
        update_relationships.direction = "content"
        update_relationships.document_type = "content"
        update_relationships.document_version = "content"
        update_relationships.document_standard = "content"
        update_relationships.document_test = "content"
        update_relationships.description = "content"
        update_relationships.test = "content"
        self.session.add(update_relationships)
        self.session.commit()

    def main(self):
        self.create_table_relationships()
        self.update_table_relationships()


if __name__ == "__main__":
    db = session_relationships("sqlite:///request_of_methods.db")
    db.main()