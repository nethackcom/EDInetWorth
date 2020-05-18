from SOAP import EdiServiceSoapEcodPl
from function_database_relationship import SessionDataBaseRelationship
from database_relationships import StructureDatabaseRelationship
from sqlalchemy.sql import select
import os

dbRelationship_object = SessionDataBaseRelationship("sqlite:///request_of_methods.db")

# Этот класс проверят есть ли строка возвращаемая из EdiServiceSoapEcodPl в базе данных. Если нет, возвращает False.
class CheckRelationshipDatabase(SessionDataBaseRelationship):
    def __init__(self):
        super(CheckRelationshipDatabase, self).__init__("sqlite:///request_of_methods.db")
        self.relation_object = EdiServiceSoapEcodPl("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")

    def CheckStringInDatabase(self):
        # Получаем словарь с xml содержимым
        xml = self.relation_object.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
        # Получаем relation-id по которому будем искать запись в базе данных.
        relation_id_check = xml[0]["relation-id"]
        # ...