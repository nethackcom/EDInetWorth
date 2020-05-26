import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from EdiDatabase import EdiDatabase
from EdiService import EdiService


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

    #  Тест №1
    print(edi_database.update_relationships(relationships))
        # INPUT: Массив с документами. Данные документа лежат в словаре.
        #        [{'relation-id': '1302672', 'partner-iln': '4606068999995', 'partner-name': 'Lenta', 'direction': 'OUT', 'document-type': 'DESADV', 'document-version': 'ECODRU20', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Ptitsefabrika ROSKAR -> DESADV -> Lenta', 'test': 'T', 'form': None}, {'relation-id': '1302673', 'partner-iln': '4606068999995', 'partner-name': 'Lenta', 'direction': 'OUT', 'document-type': 'INVOICE', 'document-version': 'RU1', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Ptitsefabrika ROSKAR -> INVOICE -> Lenta', 'test': 'T', 'form': None}, {'relation-id': '1302678', 'partner-iln': '4607164999995', 'partner-name': 'Tander', 'direction': 'OUT', 'document-type': 'DESADV', 'document-version': 'ECODRU20', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Ptitsefabrika ROSKAR -> DESADV -> Tander', 'test': 'T', 'form': None}, {'relation-id': '1302679', 'partner-iln': '4607164999995', 'partner-name': 'Tander', 'direction': 'OUT', 'document-type': 'INVOICE', 'document-version': 'RU1', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Ptitsefabrika ROSKAR -> INVOICE -> Tander', 'test': 'T', 'form': None}, {'relation-id': '1302685', 'partner-iln': '4607099139992', 'partner-name': 'OKEY', 'direction': 'OUT', 'document-type': 'DESADV', 'document-version': 'ECODRU20', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Ptitsefabrika ROSKAR -> DESADV -> OKEY', 'test': 'T', 'form': None}, {'relation-id': '1302686', 'partner-iln': '4607099139992', 'partner-name': 'OKEY', 'direction': 'OUT', 'document-type': 'INVOICE', 'document-version': 'RU1', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Ptitsefabrika ROSKAR -> INVOICE -> OKEY', 'test': 'T', 'form': None}, {'relation-id': '1302690', 'partner-iln': '4607164999995', 'partner-name': 'Tander', 'direction': 'OUT', 'document-type': 'ORDERRSP', 'document-version': 'ECODRU1', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Ptitsefabrika ROSKAR -> ORDERRSP -> Tander', 'test': 'T', 'form': None}, {'relation-id': '1302674', 'partner-iln': '4606068999995', 'partner-name': 'Lenta', 'direction': 'IN', 'document-type': 'ORDER', 'document-version': 'RU1', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Lenta -> ORDER -> Ptitsefabrika ROSKAR', 'test': 'T', 'form': None}, {'relation-id': '1302675', 'partner-iln': '4606068999995', 'partner-name': 'Lenta', 'direction': 'IN', 'document-type': 'RECADV', 'document-version': 'ECODRU', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Lenta -> RECADV -> Ptitsefabrika ROSKAR', 'test': 'T', 'form': None}, {'relation-id': '1302676', 'partner-iln': '4607164999995', 'partner-name': 'Tander', 'direction': 'IN', 'document-type': 'ORDER', 'document-version': 'RU1', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Tander -> ORDER -> Ptitsefabrika ROSKAR', 'test': 'T', 'form': None}, {'relation-id': '1302677', 'partner-iln': '4607164999995', 'partner-name': 'Tander', 'direction': 'IN', 'document-type': 'RECADV', 'document-version': 'ECODRU', 'document-standard': 'XML', 'document-test': 'T', 'description': 'Tander -> RECADV -> Ptitsefabrika ROSKAR', 'test': 'T', 'form': None}, {'relation-id': '1302683', 'partner-iln': '4607099139992', 'partner-name': 'OKEY', 'direction': 'IN', 'document-type': 'ORDER', 'document-version': 'RU1', 'document-standard': 'XML', 'document-test': 'T', 'description': 'OKEY -> ORDER -> Ptitsefabrika ROSKAR', 'test': 'T', 'form': None}, {'relation-id': '1302684', 'partner-iln': '4607099139992', 'partner-name': 'OKEY', 'direction': 'IN', 'document-type': 'RECADV', 'document-version': 'ECODRU', 'document-standard': 'XML', 'document-test': 'T', 'description': 'OKEY -> RECADV -> Ptitsefabrika ROSKAR', 'test': 'T', 'form': None}]
        # OUTPUT: Успешно

    #  Тест №2'''
    print(edi_database.update_relationships([{"relation-id": 2, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))
        # INPUT: Сгенерированный массив. Массив содержит данные одного документа.
        #       [{"relation-id": 234234, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]
        # OUTPUT: Успешно

    #  Тест №3'''
    print(edi_database.update_relationships([{"relation-id": 3, "partner-iln": "", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "", "form": ""}]))
        # INPUT: Тот же сгенерированный массив, что и в тесте №2,
        #       но я убрал данные следующих ключей словаря: partner-iln, test, form
        # OUTPUT: Успешно

    #  Тест №4'''
    print(edi_database.update_relationships([{"relation-id": 4, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}]))
        # INPUT: Всем ключам в словаре передал занчение None, кроме relation-id
        # OUTPUT: Успешно. В таблице столбцы, которые принимали None при вызове метода, пусты.

    #  Тест №5'''
    print(edi_database.update_relationships([{"relation-id": None, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))
        # INPUT: relation-id = None
        # OUTPUT: Успешно. В базе данных эта запись в столбце relation-id приняла 1

    #  Тест №6'''
    print(edi_database.update_relationships([{"relation-id": 6, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))
    print(edi_database.update_relationships([{"relation-id": 7, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))
        # INPUT: Вызов двух методов.
        # OUTPUT: Успешно. В базе данных остались данные из вызова последнего метода.

    #  Тест №7'''
    print(edi_database.update_relationships([{"relation-id": None, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": None, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))
        # INPUT: Метод принимает два одинаковых словаря с relation-id = None
        # OUTPUT: Успешно. Метод занес два документа, relation-id первому документу задал 1, второму 2.

    #  Тест №8'''
    print(edi_database.update_relationships([{"relation-id": 1, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": 1, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}]))
        # INPUT: Метод принимает два одинаковых словаря с relation-id = 1
        # OUTPUT: Успешно. Метод занес два документа, relation-id первому документу задал 1, второму 2.

    #  Тест №9'''
    print(edi_database.update_relationships([]))
        # INPUT: Передаем пустой массив
        # OUTPUT: Успешно. Не возникло не каких ошибок.

    #  Тест №10'''
    print(edi_database.get_relationships())
        # INPUT:
        # OUTPUT: Успешно. <sqlalchemy.engine.result.ResultProxy object at 0x000000ABCCF2C080>
        # При пустой таблице возвращает None