from Relationship import Relationship, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import IntegrityError
import os
from EdiService import EdiService


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
        # Наш метод update_relationships работает по принципу удалить все из таблицы изанести новые данные.
        # Сделаем обработку ошибок на случай, если возникнет ошибка при добавленни данных в таблицу Relationships.
        # С добавлением обработчика ошибок наша таблица сохранит прежние данные, а не удалит их.
        try:
            # Удаляем все из таблицы
            relation_relationships = self.get_relationships()
            for row in relation_relationships:
                delete_row = self.session.query(self.table).filter_by(relation_id=row[0]).one()
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
        except IntegrityError:
            self.session.rollback()
            raise
        finally:
            self.session.close()

    def get_relationships(self):
        """     Метод возвращает данные из таблицы      """
        with self.engine.connect() as connection:
            result = self.engine.execute(self.table_name.select())
            connection.close()
        return result


if __name__ == "__main__":
    edi_service = EdiService("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    relationships = edi_service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
    edi_database = EdiDatabase("sqlite:///request_of_methods.db")

    print(edi_database.update_relationships([{"relation-id": 1, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": 1, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))