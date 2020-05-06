# Created: 02.05.2020 9:12
# Language: Python 3.6.5
# Version: 1.0
# Copyright by Orlov Alexandr
# Documentation: https://www.esphere.ru/assets/download/WebService_Comarch%20EDI.pdf


import os
from zeep import exceptions
from zeep import Client
from zeep.transports import Transport
from requests import Session


class soap_logic(object):
    def __init__(self):
        self.wsdl = "https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL"
        self.session = Session()
        self.client = Client(self.wsdl, transport=Transport(session=self.session))

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

    # Метод обработки ошибок
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
        err = lambda errors, error: errors[error]
        print(err(errors, error))


class edi_service_soap_ecod_pl(soap_logic):
    '''
    Этот класс содержит реализацию каждого метода из EDISERVICE
    Подробнее вы можете прочить в документации https://www.esphere.ru/assets/download/WebService_Comarch%20EDI.pdf
    '''

    # Подробнее о каждом методе вы можете почитать в документации
    # (https://www.esphere.ru/assets/download/WebService_Comarch%20EDI.pdf)

    # Relationships метод
    # Данный метод возвращает взаимосвязи, определенные для конкретного пользователя в системе
    # ECOD. Взаимосвязи определяют с кем и какого типа документами обменивается пользователь.
    def Relationships(self, *data):
        relationships = self.client.service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), *data)
        self.refresh_big_data(relationships)
        print(relationships)

    # Send метод
    # Данный метод используется для посылки документов.
    def Send(self, *data):
        Send = self.client.service.Send(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), *data)
        self.refresh_big_data(Send)
        print(Send)

    # ListPB метод
    # Метод, позволяющий просмотреть статусы документов, пересылаемых в данный момент.
    def ListPB(self, *data):
        ListPB = self.client.service.ListPB(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), *data)
        self.refresh_big_data(ListPB)
        print(ListPB)

    # Receive метод
    # Метод, обеспечивающий получение документов.
    def Receive(self, *data):
        Receive = self.client.service.Receive(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), *data)
        self.refresh_big_data(Receive)
        print(Receive)

    # ListMB метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMB(self, *data):
        ListMB = self.client.service.ListMB(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), *data)
        print("Error")
        self.refresh_big_data(ListMB)
        print(ListMB)

    # ListMBex метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMBex(self, *data):
        ListMBex = self.client.service.ListMBex(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), *data)
        self.refresh_big_data(ListMBex)
        print(ListMBex)

    # ChangeDocumentStatus метод
    # Данный метод дает возможность изменить статус документа (N - new, R - read).
    def ChangeDocumentStatus(self, *data):
        ChangeDocumentStatus = self.client.service.ChangeDocumentStatus(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), *data)
        self.refresh_big_data(ChangeDocumentStatus)
        print(ChangeDocumentStatus)

    # ListPBEx метод
    # Метод возвращает значения статусов отосланных документов.
    def ListPBEx(self, *data):
        ListPBEx = self.client.service.ListPBEx(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), *data)
        self.refresh_big_data(ListPBEx)
        print(ListPBEx)


if __name__ == "__main__":
    SOAPClient = edi_service_soap_ecod_pl()
    # code is here...
    try:
        SOAPClient.Relationship(5000)
    except exceptions.ValidationError as excValid:
        print("Неверные введенные параметры метода: ", str(excValid))
    except SyntaxError as se:
        print("Введите правильность вызова метода: ", se)
    except NameError as e:
        print("Ошибка параметра: ", str(e))
    except TypeError as type_method_error:
        print(type_method_error)
    except AttributeError as att_method_error:
        print("Ошибка вызова метода: ", att_method_error)
