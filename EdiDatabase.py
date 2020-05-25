from Relationship import Relationship, Base
from sqlalchemy import create_engine, update, delete
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError


class EdiDatabase(Relationship):

    '''  Этот класс унаследует структуру базы данных Relationship
    Класс имеет два метода:
    *update_relationships(relationship)* - на входе массив с документами. Данные каждого документа лежат в словаре.
                            Метод обновляет данные в БД или заносит, если их там нет.
                            -> relationship - распарсенные данные из вызова метода EDISERVICE
    *get_relationships* - возвращает все данные Relationship из БД
    '''

    def __init__(self, url):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        self.DBSession.configure(bind=self.engine)
        self.session = self.DBSession()
        self.table = Relationship.__table__

    def update_relationships(self, relationships):
        with self.engine.connect() as connection:
            relation_relationships = self.get_relationships()  # заносим все данные из БД в массив
            for relationship in relationships:
                if len(relation_relationships) > 0:
                    for row in relation_relationships:
                        if int(relationship['relation-id']) == row[0]:
                            gg = update(self.table).where(
                                self.table.c.relation_id == relationship['relation-id']).values({
                                "relation_id": relationship['relation-id'],
                                "partner_iln": relationship['partner-iln'],
                                "partner_name": relationship['partner-name'],
                                "direction": relationship['direction'],
                                "document_type": relationship['document-type'],
                                "document_version": relationship['document-version'],
                                "document_standard": relationship['document-standard'],
                                "document_test": relationship['document-test'],
                                "description": relationship['description'],
                                "test": relationship['test'],
                                "form": relationship['form']
                            })
                            connection.execute(gg)
                        else:
                            try:
                                connection.execute(self.table.insert().values(
                                    relation_id=int(relationship['relation-id']),
                                    partner_iln=relationship['partner-iln'],
                                    partner_name=relationship['partner-name'],
                                    direction=relationship['direction'],
                                    document_type=relationship['document-type'],
                                    document_version=relationship['document-version'],
                                    document_standard=relationship['document-standard'],
                                    document_test=relationship['document-test'],
                                    description=relationship['description'],
                                    test=relationship['test'],
                                    form=relationship['form']
                                ))
                            except IntegrityError:
                                pass
                else:
                    connection.execute(self.table.insert().values(
                        relation_id=relationship['relation-id'],
                        partner_iln=relationship['partner-iln'],
                        partner_name=relationship['partner-name'],
                        direction=relationship['direction'],
                        document_type=relationship['document-type'],
                        document_version=relationship['document-version'],
                        document_standard=relationship['document-standard'],
                        document_test=relationship['document-test'],
                        description=relationship['description'],
                        test=relationship['test'],
                        form=relationship['form']
                    ))

    def get_relationships(self):
        connection = self.engine.connect()
        result = connection.execute(self.table.select())
        data_db_relationships = [elem for elem in result]
        return data_db_relationships