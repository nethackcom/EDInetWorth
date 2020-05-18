from SOAP import EdiServiceSoapEcodPl  # SOAP.py
import os  # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения
from session_relationship import SessionDataBaseRelationship


if __name__ == "__main__":

    # Test SOAP.py
    ss = EdiServiceSoapEcodPl("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    print(ss.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 5000))

    # # Test
    # db = SessionRelationship("sqlite:///request_of_methods.db")
    # db.InsertData(3451, "4562", "dfgds", "OUT", "XML", "INVDOV", "content", "gg", "tdfgdfsgest", "csdfgontent")
    # db.InsertData(3451, "3614645", "jbert", "IN", "XML", "INVDOV", "bfgsr", "tesvcx", "sdfsdg", "gfs")
    # db.InsertData(3621, "6565", "gfh", "IN", "sdv", "sfh", "wer", "wertwt", "nhg", "xcvb")

    # SessionRelationship
    db = SessionDataBaseRelationship("sqlite:///request_of_methods.db")