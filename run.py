import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from EdiDatabase import EdiDatabase
from EdiService import EdiService
from ListMB import ClassListMB
from Edi_Service_Soap_Ecod_Pl import EdiServiceSoapEcodPl

if __name__ == "__main__":
    edi_service = EdiService()
    edi_database = EdiDatabase()
    listMB =ClassListMB()
    ecod_service = EdiServiceSoapEcodPl()

    while True:
        relationships = edi_service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
        edi_database.set_relationships(relationships)
        print(ecod_service.ListMB(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "ORDER", "RU1", "XML", "T", "A", 10000))
