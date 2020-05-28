import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from EdiDatabase import EdiDatabase
from EdiService import EdiService
from unittest import TestCase

class IntegretionTest(EdiDatabase, TestCase):
    def __init__(self):
        super().__init__("sqlite:///request_of_methods.db")
        self.number_test = 1

    # Метод, который тестирует вызоваемый метод из родительского класса
    def test_update_relationships(self, relationships):
        try:
            result = False
            self.update_relationships(relationships)
            for relationship in relationships:
                exists = self.session.query(self.table).filter_by(relation_id = relationship['relation-id'])
                if exists:
                    result = True
            return relationships, result
        except Exception as e:
            print(e)
        finally:
            pass


if __name__ == "__main__":
    edi_service = EdiService("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    relationships = edi_service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
    edi_database = EdiDatabase("sqlite:///request_of_methods.db")
    IntegretionTest = IntegretionTest()

    IntegretionTest.test_update_relationships([{"relation-id": 2, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}])
    IntegretionTest.test_update_relationships([{"relation-id": 4, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}])
    IntegretionTest.test_update_relationships([{"relation-id": None, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}])
    IntegretionTest.test_update_relationships([{"relation-id": None, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": None, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}])
    IntegretionTest.test_update_relationships([{"relation-id": 1, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": 1, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}])
    IntegretionTest.test_update_relationships([])
