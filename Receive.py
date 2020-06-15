import Relationship
from Relationship import Relationship as table
from sqlalchemy.orm import sessionmaker
from EdiService import EdiService
from ListMB import ListMB
import os

# Функция записи данных из вызова Receive метода в файл
def write_receive_to_file(data):
    for document in data:
        with open("", "w") as file:  # Нужно будет доделать, когда метод ListMB будет возвращать данные
            file.write(str(data))


class Receive(EdiService, ListMB):
    def __init__(self):
        super().__init__()
        Session = sessionmaker(bind=Relationship.engine)
        self.session = Session()
        self.table = table
        self.table_name = table.__table__

    def callReceive(self, relationships):
        """ Метод вызывает метод Receive.
            Возвращаемые данные из вызова метода Receive записывает в файл.
            Для каждого документа свой файл со своим названием
        """
        data_receive = []
        data_list_mb = self.callListMB()
        for relationship, document_list_mb in zip(relationships, data_list_mb):
            data_receive.append(self.Receive(
                os.getenv("NAME_KEY"),
                os.getenv("PASSWORD_KEY"),
                relationship['partner-iln'],
                relationship["document-type"],
                document_list_mb['tracking-id'],
                relationship["document-standard"],
                "N",
                10000
            ))

        return write_receive_to_file(data_receive)