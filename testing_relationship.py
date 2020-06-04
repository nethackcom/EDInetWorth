from EdiDatabase import EdiDatabase
import unittest

''' Запуск теста relationship
    Установите библиотеку unittest.
    Для начала нужно перейти в коренвую папку файла.
    Для запуска теста нужно в консоле ввести команду: python -m unittest testing_relationship.py
    Для более детального отчета можете ввести команду: python -m unittest -v testing_relationship.py
'''

class TestRelationships(unittest.TestCase):
    """ Тестирование добавления в таблицу входящих данных.
        Реализация добавления данных в таблицу находится в EdiDatabase.py(class EdiDatabase).

        Unittest
        Название каждого тестового кейса должно начинаться с test.
        При вызове unittest.main(), все методы в классе TestRelationships, которых название начинается с test, будут вызванны и протестированны.

        Логика тестовых кейсов:
        Метод set_relationships обновляет данные в таблице Relationships и входящие данные. Заносим эти данные в переменную relationships.
        В переменной relationships_from_db хранятся данные из таблицы.
        Метод self.assertEqual сравнивание два аргумента между собой. При неравенстве выкидывает принт сравнения и объяснение неравенства.

        Сравнивание relationships и relationships_from_db используется для того, чтобы проверить занеслись ли передаваемые данные в таблицу.

        Все тестовые кейсы не зависят от выполнения предыдущего тестового кейса.
    """
    # Этот метод вызывается для каждого выполняемого тестового кейса
    @classmethod
    def setUpClass(cls):
        cls.edi_database = EdiDatabase("sqlite:///request_of_methods.db")

    # Проверяем заносит ли, в таблицу передаваемые данные
    def test_1(self):
        relationships = [{"relation-id": 2, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}]
        self.edi_database.set_relationships(relationships)
        relationships_from_db = self.edi_database.get_relationships()
        self.assertEqual(relationships, relationships_from_db)

    # Проверяем занесет ли, передаваемые данные с None аргументом, но relation-id = 4
    def test_2(self):
        relationships = [{"relation-id": 4, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}]
        self.edi_database.set_relationships(relationships)
        relationships_from_db = self.edi_database.get_relationships()
        self.assertEqual(relationships, relationships_from_db)

    # Проверяем правильность занесения данных со всеми аргументами None
    def test_3(self):
        relationships_from_db_before_update = self.edi_database.get_relationships()
        try:
            relationships = [{"relation-id": None, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}]
            call_method = self.edi_database.set_relationships(relationships)
        except Exception:
            relationships_from_db_after_update = self.edi_database.get_relationships()
            self.assertEqual(relationships_from_db_before_update, relationships_from_db_after_update)

    def test_4(self):
        relationships = [{"relation-id": None, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}]
        call_method = self.edi_database.set_relationships(relationships)
        relationships_from_db = self.edi_database.get_relationships()

    def test_5(self):
        relationships_from_db_before_update = self.edi_database.get_relationships()
        try:
            relationships = [{"relation-id": None, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}]
            self.edi_database.set_relationships(relationships)
        except Exception:
            relationships_from_db_after_update = self.edi_database.get_relationships()
            self.assertEqual(relationships_from_db_before_update, relationships_from_db_after_update)

    def test_6(self):
        relationships = [{"relation-id": None, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}]
        call_method = self.edi_database.set_relationships(relationships)
        relationships_from_db = self.edi_database.get_relationships()

    # Проверяем выдаст ли ошибку при одинаковом relation-id у 2-х документов
    def test_7(self):
        relationships_from_db_before_update = self.edi_database.get_relationships()
        try:
            relationships = [{"relation-id": 1, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}, {"relation-id": 1, "partner-iln": "", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}]
            self.edi_database.set_relationships(relationships)
        except Exception:
            relationships_from_db_after_update = self.edi_database.get_relationships()
            self.assertEqual(relationships_from_db_before_update, relationships_from_db_after_update)

    def test_8(self):
        relationships = [{"relation-id": 1, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}, {"relation-id": 1, "partner-iln": "", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}]
        call_method = self.edi_database.set_relationships(relationships)
        relationships_from_db = self.edi_database.get_relationships()
        self.assertRaises(Exception, call_method)  # Проверяем на исключения

    # Проверяем очистит ли базу данных при передачи пустого массива с документами
    def test_9(self):
        relationships = []
        self.edi_database.set_relationships(relationships)
        relationships_from_db = self.edi_database.get_relationships()
        self.assertEqual(relationships, relationships_from_db)


if __name__ == "__main__":
    unittest.main()  # запускаем наш класс с тестовыми кейсами