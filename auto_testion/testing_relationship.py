from EdiDatabase import EdiDatabase

class IntegretionTest(EdiDatabase):
    def __init__(self):
        super().__init__("sqlite:///request_of_methods.db")

    def test_update_relationships(self, relationships):
        # Так как тестовые кейсы не должны зависить друг от друга,
        # отлавливаем исключения и продолжаем тестить дальше
        try:
            result = False
            self.update_relationships(relationships)
            for relationship in relationships:
                exists = self.session.query(self.table).filter_by(relation_id=relationship['relation-id'])
                if exists:
                    result = True
            return relationships, result  # Возвращаем входящие данные для теста и результат теста
        except Exception as e:
            return e, relationships
        finally:
            pass


if __name__ == "__main__":
    edi_database = EdiDatabase("sqlite:///request_of_methods.db")
    IntegretionTest = IntegretionTest()

    IntegretionTest.test_update_relationships([{"relation-id": 2, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}])
    IntegretionTest.test_update_relationships([{"relation-id": 4, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}])
    IntegretionTest.test_update_relationships([{"relation-id": None, "partner-iln": "sdfgdsfg", "partner-name": "sdfgdsfg", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}])
    IntegretionTest.test_update_relationships([{"relation-id": None, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": None, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}])
    IntegretionTest.test_update_relationships([{"relation-id": 1, "partner-iln": "sdfgdsfg", "partner-name": "dfgh", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}, {"relation-id": 1, "partner-iln": "", "partner-name": "gdfe", "direction": "sdfgdsfg", "document-type": "sdfgdsfg", "document-version": "sdfgdsfg", "document-standard": "sdfgdsfg", "document-test": "sdfgdsfg", "description": "sdfgdsfg", "test": "sdfgdsfg", "form": "sdfgdsfg"}])
    IntegretionTest.test_update_relationships([])
