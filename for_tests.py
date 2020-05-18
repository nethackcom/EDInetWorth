from database_relationships import session_relationships  # database_relationships.py
from SOAP import edi_service_soap_ecod_pl  # SOAP.py
import os # Импортируем эту библиотеку для получения секьюрити данных из переменных окружения


if __name__ == "__main__":

    # Test SOAP.py
    ss = edi_service_soap_ecod_pl("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    print(ss.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 5000))

    # Test
    db = session_relationships("sqlite:///request_of_methods.db")
    db.select_data_relationships(3451, "4562", "dfgds", "OUT", "XML", "INVDOV", "content", "gg", "tdfgdfsgest", "csdfgontent")
    db.select_data_relationships(3451, "3614645", "jbert", "IN", "XML", "INVDOV", "bfgsr", "tesvcx", "sdfsdg", "gfs")
    db.update_table_relationships(3621, "6565", "gfh", "IN", "sdv", "sfh", "wer", "wertwt", "nhg", "xcvb")