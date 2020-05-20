from Relationship import Relationship, Base
from sqlalchemy import create_engine, update, delete
from sqlalchemy.orm import sessionmaker


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

    def update_relationships(self, relationship):
        with self.engine.connect() as connection:
            a = connection.execute(self.table.select())  # заносим все данные из БД в массив
            start_data_bd = [elem.relation_id for elem in a]  # получаем все relation_id из массива с данными БД
            for i in range(len(relationship)):
                if int(relationship[i]['relation-id']) not in start_data_bd:
                    connection.execute(self.table.insert().values(
                        relation_id=relationship[i]['relation-id'],
                        partner_iln=relationship[i]['partner-iln'],
                        partner_name=relationship[i]['partner-name'],
                        direction=relationship[i]['direction'],
                        document_type=relationship[i]['document-type'],
                        document_version=relationship[i]['document-version'],
                        document_standard=relationship[i]['document-standard'],
                        document_test=relationship[i]['document-test'],
                        description=relationship[i]['description'],
                        test=relationship[i]['test'],
                        form=relationship[i]['form'],
                    ))
                else:
                    gg = update(self.table).where(self.table.c.relation_id == relationship[i]['relation-id']).values({
                        "relation_id": relationship[i]['relation-id'],
                        "partner_iln": relationship[i]['partner-iln'],
                        "partner_name": relationship[i]['partner-name'],
                        "direction": relationship[i]['direction'],
                        "document_type": relationship[i]['document-type'],
                        "document_version": relationship[i]['document-version'],
                        "document_standard": relationship[i]['document-standard'],
                        "document_test": relationship[i]['document-test'],
                        "description": relationship[i]['description'],
                        "test": relationship[i]['test'],
                        "form": relationship[i]['form']
                    })
                    connection.execute(gg)
                # b = connect.execute(self.table.select())
                # end_data_bd = [elem for elem in b]
                # for b_elem in end_data_bd:
                #     for a_elem in start_data_bd:
                #         if a_elem not in b_elem:
                #             ss = self.session.query(self.table).delete(self.table.c.relation_id==a_elem.relation_id)
                #             self.session.add(ss)
                #             self.session.commit()

    def get_relationships(self):
        with self.engine.connect() as connection:
            result = connection.execute(self.table.select())
            return result