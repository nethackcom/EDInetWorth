import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from EdiDatabase import EdiDatabase
from EdiService import EdiService

if __name__ == "__main__":
    edi_service = EdiService("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    relationships = edi_service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
    edi_database = EdiDatabase("sqlite:///request_of_methods.db")

    print(edi_database.update_relationships(relationships))  # None
    print(edi_database.get_relationships())  # <sqlalchemy.engine.result.ResultProxy object at 0x00000029EE73FF98>