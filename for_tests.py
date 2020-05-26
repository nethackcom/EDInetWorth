import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from EdiDatabase import EdiDatabase
from EdiService import EdiService


if __name__ == "__main__":

    ''' Создаем обьекты классов '''
    edi_service = EdiService("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    relationships = edi_service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
    edi_database = EdiDatabase("sqlite:///request_of_methods.db")

    ''' Тест №1'''
    print(edi_database.update_relationships(relationships))
    print(edi_database.update_relationships([{"relation-id": 234234, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))
    ''' Об тестировании №1
        Вызываем два раза один и тот же метод, но передаем разные аргументы.
        
        В первом вызове update_relationships передаем массив с документами. Данные каждого документа лежат в словаре.
        Из таблицы удаляются все данные после чего
        в таблицу заносятся все данные которые, были переданные в качестве аргумента.
        
        Во втором вызове update_relationships передаем сгенерированный массив с данными одного документа в dict.
        Из таблицы удаляются все данные и заносится наши сгенерированные данные.
    '''

    ''' Тест №2'''
    print(edi_database.update_relationships([{"relation-id": 234234, "partner-iln": "", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": ""}]))
    ''' Об тестировании №2
        Передали сгенерированные данные, но аргументы partner_iln и form оставил пустыми
        Такой вызов ошибок не вызвал
    '''