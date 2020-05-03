# Created: 02.05.2020 9:12
# Language: Python 3.6.5
# Version: 1.0
# Copyright by Orlov Alexandr


import os
from zeep import Client
from zeep.transports import Transport
from requests import Session

class SOAP(object):

    def __init__(self):
        self.wsdl = "https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL"
        self.session = Session()
        self.client = Client(self.wsdl, transport=Transport(session=self.session))

        # В переменную big_data заносятся большинство данных вызываемого метода.
        # Это сделанно для того, чтобы создать некий канал связи между всеми обьектами в классе SOAP.
        # Переменную обновляет обьект refresh_big_data(), после вызова любого метода веб-сервиса
        self.big_data = \
        {
            "code_error": None,
            "PartnerIln": None,
            "DocumentType": None,
            "DocumentVersion": None,
            "DocumentStandard": None,
            "DocumentTest": None,
            "TrackingId": None
        }

    def Relationships(self, *data):
        request_data = data
        relationships = self.client.service.Relationships(*request_data)
        self.refresh_big_data(relationships)
        print(relationships)

    def Send(self, *data):
        request_data = data
        Send = self.client.service.Send(*request_data)
        self.refresh_big_data(Send)
        print(Send)

    def ListPB(self, *data):
        request_data = data
        ListPB = self.client.service.ListPB(*request_data)
        self.refresh_big_data(ListPB)
        print(ListPB)

    def Receive(self, *data):
        request_data = data
        Receive = self.client.service.Receive(*request_data)
        self.refresh_big_data(Receive)
        print(Receive)

    def ListMB(self, *data):
        request_data = data
        ListMB = self.client.service.ListMB(*request_data)
        self.refresh_big_data(ListMB)
        print(ListMB)

    def ListMBex(self, *data):
        request_data = data
        ListMBex = self.client.service.ListMBex(*request_data)
        self.refresh_big_data(ListMBex)
        print(ListMBex)

    def ChangeDocumentStatus(self, *data):
        request_data = data
        ChangeDocumentStatus = self.client.service.ChangeDocumentStatus(*request_data)
        self.refresh_big_data(ChangeDocumentStatus)
        print(ChangeDocumentStatus)

    def ListPBEx(self, *data):
        request_data = data
        ListPBEx = self.client.service.ListPBEx(*request_data)
        self.refresh_big_data(ListPBEx)
        print(ListPBEx)



    def refresh_big_data(self, updates):
        self.big_data = \
            {
                "code_error": updates["Res"],
                "PartnerIln": None,  # updates["partner-iln"]
                "DocumentType": None,  # updates["document-type"]
                "DocumentVersion": None,  # updates["document-version"]
                "DocumentStandard": None,  # updates["document-standard"]
                "DocumentTest": None,  # updates["document-test"]
                "TrackingId": None  # updates["tracking-id"]
            }
        self.trackback_errors()

    def trackback_errors(self):
        errors = {
            "00000000": "Операция успешно завершена.",
            "00000001": "Ошибка аутентификации.",
            "00000002": "Ошибка во взаимосвязи.",
            "00000003": "Внешняя ошибка.",
            "00000004": "Внутренняя ошибка сервера.",
            "00000005": "Превышен таймаут на выполнение метода.",
            "00000006": "Ошибка Web.",
            "00000007": "Некорректные параметры."
        }
        error = str(self.big_data["code_error"])
        # print([errors[err] for err in errors if err == error])
        err = lambda errors, error: errors[error]
        print(err(errors, error))


if __name__ == "__main__":
    SOAPClient = SOAP()
    # code is here...
    
    SOAPClient.Relationships("2000000006", "password", 5000)
    SOAPClient.Send("2000000000006", "password", "2000000000009", "INVOICE", "ECODV0R2", "EDIFACT", "T", "0001", "UNB ... UNZ", 5000)
