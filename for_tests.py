from Edi_Service_Soap_Ecod_Pl import EdiServiceSoapEcodPl  # SOAP.py
import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from EdiDatabase import EdiDatabase
from EdiService import EdiService


if __name__ == "__main__":

    # Test SOAP.py
    # ss = EdiServiceSoapEcodPl("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    # print(ss.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 5000))

    # SessionRelationship
    # db = EdiDatabase("sqlite:///request_of_methods.db")
    # db.InsertData(5625, "4562", "dfgds", "OUT", "XML", "INVDOV", "content", "gg", "tdfgdfsgest", "csdfgontent", "None")
    # db.InsertData(254645, "3614645", "jbert", "IN", "XML", "INVDOV", "bfgsr", "tesvcx", "sdfsdg", "gfs", "None")
    # db.InsertData(25436, "6565", "gfh", "IN", "sdv", "sfh", "wer", "wertwt", "nhg", "xcvb", "None")
    # db.update_relationships()

    # EdiService
    # ediservice = EdiService("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    # print(ediservice.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000))
    # print(ediservice.Send(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "DESADV", "ECODRU20", "XML", "T", "sdf", "sdf", 5000))
    # print(ediservice.ListPB(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "DESADV", "ECODRU20", "XML", "T", "", "", "", "", 5000))
    # print(ediservice.Receive(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "None", "ECODRU20", "XML", "R", 5000))
    # print(ediservice.ListMB(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "DESADV", "ECODRU20", "XML", "T", "A", 5000))
    # print(ediservice.ListMBex(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "DESADV", "ECODRU20", "XML", "T", "", "", "", "", "A", 5000))
    # print(ediservice.ChangeDocumentStatus(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "DESADV", "ECODRU20", "XML", "T", "sdf", "sdf", 5000))
    # print(ediservice.ListPBEx(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), "4606068999995", "DESADV", "ECODRU20", "XML","T", "sdf", "sdf", 5000))

    edi_service = EdiService("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    relationships = edi_service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 1000)
    # print(relationship)

    edi_database = EdiDatabase("sqlite:///request_of_methods.db")
    print(edi_database.update_relationships(relationships))
    print(edi_database.get_relationships())
