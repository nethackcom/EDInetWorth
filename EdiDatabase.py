from Relationship import Relationship, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class EdiDatabase(Relationship):

    '''  Этот класс унаследует структуру базы данных Relationship
    Класс имеет два метода:
    *update_relationships(relationship)* - на входе массив с документами. Данные каждого документа лежат в словаре.
                            Метод удаляет все с базы данных и заносит новые данные.
    *get_relationships* - возвращает все данные Relationship из БД
    '''

    def __init__(self, url):
        self.engine = create_engine(url)
        Base.metadata.create_all(self.engine)
        Base.metadata.bind = self.engine
        self.DBSession = sessionmaker(bind=self.engine)
        self.DBSession.configure(bind=self.engine)
        self.session = self.DBSession()
        self.table = Relationship
        self.table_name = Relationship.__table__

    def update_relationships(self, relationships):
        """ Метод принимает
            -> relationships расперсенные данные из вызова методов EDISERVICE
        """
        relation_relationships = self.get_relationships()
        for row in relation_relationships:
            delete_row = self.session.query(self.table).filter_by(relation_id=row[0]).one()
            self.session.delete(delete_row)
        self.session.commit()
        for relationship in relationships:
            add_row = self.table(
                relationship['relation-id'],
                relationship['partner-iln'],
                relationship['partner-name'],
                relationship['direction'],
                relationship['document-type'],
                relationship['document-version'],
                relationship['document-standard'],
                relationship['document-test'],
                relationship['description'],
                relationship['test'],
                relationship['form'],
            )
            self.session.add(add_row)
        self.session.commit()

    def get_relationships(self):
        result = self.engine.execute(self.table_name.select())
        return result