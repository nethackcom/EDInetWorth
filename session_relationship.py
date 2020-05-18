from database_relationships import StructureDatabaseRelationship, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class SessionDataBaseRelationship:

    def __init__(self, url):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def InsertData(self, relation_id_value, partner_iln_value, partner_name_value, direction_value, document_type_value, document_version_value, document_standard_value, document_test_value, description_value, test_value):
        fop = StructureDatabaseRelationship(relation_id=relation_id_value, partner_iln=partner_iln_value, partner_name=partner_name_value, direction=direction_value,
                        document_type=document_type_value, document_version=document_version_value, document_standard=document_standard_value, document_test=document_test_value,
                        description=description_value, test=test_value)
        self.session.add(fop)
        self.session.commit()