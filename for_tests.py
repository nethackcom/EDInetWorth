import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from EdiDatabase import EdiDatabase
from EdiService import EdiService
from unittest import TestCase

class IntegretionTest(EdiDatabase, TestCase):
    def __init__(self):
        super().__init__("sqlite:///request_of_methods.db")
        self.number_test = 1
        self.before_row_count = 0

    def test(self, update_relationships):
        data_from_table = self.engine.execute(self.table_name.select())
        print("\n")
        print("Тестирование " + str(self.number_test) + ":")
        print("Количество записей в таблице Relationships до вызова:", str(self.before_row_count))
        print("Количество записей в таблице Relationships после вызова:", self.session.query(self.table).count())
        if not self.assertRaises(Exception, update_relationships):
            print("Статус выполнения теста: Ошибка", update_relationships)
        else:
            print("Статус выполнения теста: Успешно")
            print("Данные из таблицы:")
            print("******")
            print([elem for elem in data_from_table])
            print("******")
        self.before_row_count = self.session.query(self.table).count()
        self.number_test += 1


if __name__ == "__main__":

    '''
        Метод update_relationships принимает массив с документами. Данные каждого документа лежат в словаре.
        Метод update_relationships удаляет все данные из таблицы БД и заносит
        входящие аргументы в таблицу Relationships 

        Метод get_relationships возвращает все данные из таблицы Relationships

        OUTPUT имеет два статуса.
        :: Успешно -> означает, что метод работает так как задумывалось разработчиком, без ошибок и исключений.
        :: Исправленно -> означает, что были ошибки, но они исправленны.

    '''

    #  Создаем обьекты классов
    edi_service = EdiService("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    relationships = edi_service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
    edi_database = EdiDatabase("sqlite:///request_of_methods.db")
    IntegretionTest = IntegretionTest()

    #  Тест №1'''
    IntegretionTest.test(edi_database.update_relationships([{"relation-id": 2, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))

    #  Тест №2'''
    IntegretionTest.test(edi_database.update_relationships([{"relation-id": 4, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}]))

    #  Тест №3'''
    IntegretionTest.test(edi_database.update_relationships([{"relation-id": None, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))

    #  Тест №4'''
    IntegretionTest.test(edi_database.update_relationships([{"relation-id": None, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": None, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))

    #  Тест №5'''
    IntegretionTest.test(edi_database.update_relationships([{"relation-id": 1, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": 1, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))

    #  Тест №6'''
    IntegretionTest.test(edi_database.update_relationships([]))