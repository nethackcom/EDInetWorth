import Relationship
from Relationship import Relationship as table
from sqlalchemy.orm import sessionmaker
from EdiService import EdiService
import os


class ListMB(EdiService):
    def __init__(self):
        super().__init__()
        Session = sessionmaker(bind=Relationship.engine)
        self.session = Session()
        self.table = table
        self.table_name = table.__table__

    def callListMB(self):
        data_list_mb = []
        for relationship in self.session.query(self.table).filter_by(direction="IN").all():
            data_list_mb.append(self.ListMB(
                os.getenv("NAME_KEY"),
                os.getenv("PASSWORD_KEY"),
                relationship.partner_iln,
                relationship.document_type,
                relationship.document_version,
                relationship.document_standard,
                relationship.document_test,
                "A",
                10000
            ))
        return data_list_mb
