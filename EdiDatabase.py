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
        """ Метод update_relationships принимает массив с документами.
            Данные каждого документа лежат в словаре.
            Метод update_relationships удаляет все данные из таблицы БД и заносит
            входящие аргументы в таблицу Relationships
        """
        # Удаляем все из таблицы
        relation_relationships = self.get_relationships()
        for row in relation_relationships:
            delete_row = self.session.query(self.table).filter_by(relation_id=row[0]).one()
            self.session.delete(delete_row)
        self.session.commit()

        # Цикл удаления дублирующих словарей по relation-id из массива relationships
        index = 1
        for relationship in relationships:
            for x in range(index, len(relationships)):
                if relationship['relation-id'] == relationships[x]['relation-id']:
                    del relationships[x]
            index += 1

        # Добавляем данные документов из relationships в массив
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
        """     Метод возвращает данные из таблицы      """
        result = self.engine.execute(self.table_name.select())
        return result