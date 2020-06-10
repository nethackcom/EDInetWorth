import Relationship
from Relationship import Relationship as table
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import ArgumentError

class EdiDatabase(table):

    '''  Этот класс унаследует структуру базы данных Relationship
    Класс имеет два метода:
    *set_relationships(relationship)* - на входе массив с документами. Данные каждого документа лежат в словаре.
                            Метод обновляет данные в таблице Relationships.
    *get_relationships* - возвращает все данные Relationship из БД
    '''

    def __init__(self):
        Session = sessionmaker(bind=Relationship.engine)
        self.session = Session()
        self.table = table
        self.table_name = table.__table__

    def set_relationships(self, relationships):
        """ Метод set_relationships принимает массив с документами.
            Данные каждого документа лежат в словаре.
            Этот метод обновляет данны в таблице Relationships
        """
        self.__check_documents(relationships)

        # Удаляем все из таблицы
        relation_relationships = self.get_relationships()
        for row in relation_relationships:
            delete_row = self.session.query(self.table).filter_by(relation_id=row['relation-id']).one()
            self.session.delete(delete_row)

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
        self.session.close()

    def get_relationships(self):
        """     Метод возвращает данные из таблицы      """
        with Relationship.engine.connect() as connection:
            result = Relationship.engine.execute(self.table_name.select())
            table_data = []
            for elem in result:
                table_data.append({
                    'relation-id': elem[0],
                    'partner-iln': elem[1],
                    'partner-name': elem[2],
                    'direction': elem[3],
                    'document-type': elem[4],
                    'document-version': elem[5],
                    'document-standard': elem[6],
                    'document-test': elem[7],
                    'description': elem[8],
                    'test': elem[9],
                    'form': elem[10],
                })
            connection.close()
            # Так как реляционная база данных не гарантирует возвращение отсортированных данных, сортируем их.
            table_data_sorted = sorted(table_data, key=lambda x: x['relation-id'])
        return table_data_sorted

    def __check_documents(self, relationships):

        # Проверка relation-id каждого документа.Если relation-id = None, то выпрыгнет Exception
        if relationships:
            for relationship in relationships:
                if relationship and relationship['relation-id'] is None:
                    raise ArgumentError('Invalid relation-id -> {}'.format(relationship['relation-id']), relationship)
