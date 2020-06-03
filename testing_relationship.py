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
        Метод update_relationships обновляет данные в таблице Relationships и входящие данные. Заносим эти данные в переменную database.
        В переменной get_table_data хранятся данные из таблицы.
        Метод self.assertEqual сравнивание два аргумента между собой. При неравенстве выкидывает принт сравнения и объяснение неравенства.

        Сравнивание relationships и get_table_data используется для того, чтобы проверить занеслись ли передаваемые данные в таблицу.

        Все тестовые кейсы не зависят от выполнения предыдущего тестового кейса.
    """
    # Этот метод вызывается для каждого выполняемого тестового кейса
    @classmethod
    def setUpClass(cls):
        cls.edi_database = EdiDatabase("sqlite:///request_of_methods.db")

    # Проверяем заносит ли, в таблицу передаваемые данные
    def test_1(self):
        relationships = [{"relation-id": 2, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}]
        self.edi_database.update_relationships(relationships)
        get_table_data = self.edi_database.get_relationships()
        self.assertEqual(relationships, get_table_data)

    # Проверяем занесет ли, передаваемые данные с None аргументом, но relation-id = 4
    def test_2(self):
        database = self.edi_database.update_relationships([{"relation-id": 4, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}])
        get_table_data = self.edi_database.get_relationships()
        self.assertEqual(database, get_table_data)

    # Проверяем правильность занесения данных со всеми аргументами None
    def test_3(self):
        database = self.edi_database.update_relationships([{"relation-id": None, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}])
        get_table_data = self.edi_database.get_relationships()
        self.assertEqual(get_table_data, [{"relation-id": 5, "partner-iln": None, "partner-name": None, "direction": None, "document-type": None, "document-version": None, "document-standard": None, "document-test": None, "description": None, "test": None, "form": None}])

    def test_4(self):
        database = self.edi_database.update_relationships([{"relation-id": None, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}])
        get_table_data = self.edi_database.get_relationships()
        self.assertEqual(get_table_data, [{"relation-id": 6, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}])

    # Проверяем правильность занесения данных 2-х документов со аргументами relation-id = None
    def test_5(self):
        input_data = self.edi_database.update_relationships([{"relation-id": None, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}, {"relation-id": None, "partner-iln": "", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}])
        get_table_data = self.edi_database.get_relationships()
        self.assertEqual(get_table_data, [{"relation-id": 7, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}, {"relation-id": 8, "partner-iln": "", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}])

    # Проверяем выдаст ли ошибку при одинаковом relation-id у 2-х документов
    def test_6(self):
        database = self.edi_database.update_relationships([{"relation-id": 1, "partner-iln": "test", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}, {"relation-id": 1, "partner-iln": "", "partner-name": "test", "direction": "test", "document-type": "test", "document-version": "test", "document-standard": "test", "document-test": "test", "description": "test", "test": "test", "form": "test"}])
        get_table_data = self.edi_database.get_relationships()
        self.assertRaises(Exception, database)  # Проверяем на исключения

    # Проверяем очистит ли базу данных при передачи пустого массива с документами
    def test_7(self):
        database = self.edi_database.update_relationships([])
        get_table_data = self.edi_database.get_relationships()
        self.assertEqual(database, get_table_data)


if __name__ == "__main__":
    unittest.main()  # запускаем наш класс с тестовыми кейсами
