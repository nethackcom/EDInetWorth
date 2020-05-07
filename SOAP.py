# Created: 02.05.2020 9:12
# Language: Python 3.6.5
# Version: 1.0
# Copyright by Orlov Alexandr
# Documentation: https://www.esphere.ru/assets/download/WebService_Comarch%20EDI.pdf


import os
from zeep import exceptions
from zeep import Client
from zeep.transports import Transport
import requests.exceptions
from requests import Session


# Класс по обработке и вывода сообщений
class TrackbackMessage(object):
    def trackback_errors(self, request_data):
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

        error = str(request_data["Res"])
        err = lambda errors, error: errors[error]
        print(err(errors, error))


class edi_service_soap_ecod_pl(TrackbackMessage):
    '''
    Этот класс содержит реализацию каждого метода из EDISERVICE
    Подробнее вы можете прочить в документации https://www.esphere.ru/assets/download/WebService_Comarch%20EDI.pdf
    Описание параметров:
    <::Тип_переменной -> параметр -> Описание параметра>
    ::str -> partner_iln -> ID партнера, которому будет посылаться документ
    ::str -> document_type -> Тип документа
    ::str -> document_version -> Версия спецификации
    ::str -> document_standard -> Стандарт документа
    ::str -> document_test -> Статус документа (T – тест, P – продукционный)
    ::str -> control_number -> Контрольный номер документа
    ::str -> document_content -> Содержание документа
    ::str -> date_from -> Опциональный
    ::str -> date_to -> Опциональный
    ::str -> item_from -> Опциональный
    ::str -> item_to -> Опциональный
    ::str -> tracking_id -> Document identifier in ECOD system (in data base BTS)
    ::str -> change_document_status -> Новый статус документа после завершения чтения документа (new(N) или read(R))
    ::str -> status -> Новый статус документа
    ::str -> order_by ->
    ::int -> timeout -> Таймаут на выполнение вызова метода(мс)
    '''

    def __init__(self):
        self.wsdl = "https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL"
        self.session = Session()
        self.client = Client(self.wsdl, transport=Transport(session=self.session))

    # Relationships метод
    # Данный метод возвращает взаимосвязи, определенные для конкретного пользователя в системе
    # ECOD. Взаимосвязи определяют с кем и какого типа документами обменивается пользователь.
    def Relationships(self, timeout):
        request_data = self.client.service.Relationships(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), timeout)
        self.trackback_errors(request_data)
        print(request_data)


    # Send метод
    # Данный метод используется для посылки документов.
    def Send(self, partner_iln, document_type, document_version, document_standard, document_test, control_number, document_content, timeout):
        request_data = self.client.service.Send(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), partner_iln, document_type, document_version, document_standard, document_test, control_number, document_content, timeout)
        self.trackback_errors(request_data)
        print(request_data)

    # ListPB метод
    # Метод, позволяющий просмотреть статусы документов, пересылаемых в данный момент.
    def ListPB(self, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, timeout):
        request_data = self.client.service.ListPB(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, timeout)
        self.trackback_errors(request_data)
        print(request_data)

    # Receive метод
    # Метод, обеспечивающий получение документов.
    def Receive(self, partner_iln, document_type, tracking_id, document_standard, change_document_status, timeout):
        request_data = self.client.service.Receive(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), partner_iln, document_type, tracking_id, document_standard, change_document_status, timeout)
        self.trackback_errors(request_data)
        print(request_data)

    # ListMB метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMB(self, partner_iln, document_type, document_version, document_standard, document_test, document_status, timeout):
        request_data = self.client.service.ListMB(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), partner_iln, document_type, document_version, document_standard, document_test, document_status, timeout)
        self.trackback_errors(request_data)
        print(request_data)

    # ListMBex метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMBex(self, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, document_status, timeout):
        request_data = self.client.service.ListMBex(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, document_status, timeout)
        self.trackback_errors(request_data)
        print(request_data)

    # ChangeDocumentStatus метод
    # Данный метод дает возможность изменить статус документа (N - new, R - read).
    def ChangeDocumentStatus(self, tracking_id, status):
        request_data = self.client.service.ChangeDocumentStatus(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), tracking_id, status)
        self.trackback_errors(request_data)
        print(request_data)

    # ListPBEx метод
    # Метод возвращает значения статусов отосланных документов.
    def ListPBEx(self, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout):
        request_data = self.client.service.ListPBEx(os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout)
        self.trackback_errors(request_data)
        print(request_data)


if __name__ == "__main__":
    try:
        SOAPClient = edi_service_soap_ecod_pl()
        SOAPClient.Relationships(5000)
        # code is here...

    except exceptions.ValidationError:
        raise
    except requests.exceptions.ConnectionError:
        raise
    except SyntaxError as se:
        raise
    except NameError:
        raise
    except TypeError:
        raise
    except AttributeError:
        raise
