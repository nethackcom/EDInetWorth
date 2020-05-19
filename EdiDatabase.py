from Relationship import Relationship, Base
from sqlalchemy import create_engine, select, update, delete
from sqlalchemy.orm import sessionmaker
from EdiService import EdiService


class EdiDatabase():

    def __init__(self, url):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        self.session = self.DBSession()

    def update_relationships(self, relationship):
        table = Relationship.__table__
        stmp = update(table).where(table.c.relation_id == relationship[0]['relation-id']).values(
            relation_id=relationship[0]['relation-id'],
            partner_iln=relationship[0]['partner-iln'],
            partner_name=relationship[0]['partner-name'],
            direction=relationship[0]['direction'],
            document_type=relationship[0]['document-type'],
            document_version=relationship[0]['document-version'],
            document_standard=relationship[0]['document-standard'],
            document_test=relationship[0]['document-test'],
            description=relationship[0]['description'],
            test=relationship[0]['test'],
            form=relationship[0]['form']
        )
        conn = self.engine.connect()
        r = conn.execute(stmp)
        conn.close()
        print(relationship)
        # q = select([table.c.relation_id]).where(table.c.relation_id == relationship[0]['relation-id'])
        # conn = self.engine.connect()
        # r = conn.execute(q)
        # state = r.fetchall()
        # conn.close()
        # print(relationship)
        # return state

    def get_relationships(self):
        q = self.session.query(Relationship)