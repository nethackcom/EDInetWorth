import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from EdiDatabase import EdiDatabase
from EdiService import EdiService
from ListMB import ListMB
from Edi_Service_Soap_Ecod_Pl import EdiServiceSoapEcodPl

if __name__ == "__main__":
    edi_service = EdiService()
    edi_database = EdiDatabase()
    listMB =ListMB()
    ecod_service = EdiServiceSoapEcodPl()

    relationships = edi_service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
    edi_database.set_relationships(relationships)
    print(edi_service.ListMB(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "ORDER", "RU1", "XML", "T", "A", 10000))
    print(listMB.callListMB())