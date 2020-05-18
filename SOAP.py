# Language: Python 3.6.5
# Version: 1.6
# Author: Orlov Alexandr
# Documentation: https://www.esphere.ru/assets/download/WebService_Comarch%20EDI.pdf

from parse_requst_data import ParseRequestDataXML
from zeep import Client
from zeep.transports import Transport
from requests import Session


class EdiServiceSoapEcodPl:
    '''
    Этот класс содержит реализацию каждого метода из EDISERVICE
    Подробнее вы можете прочить в документации https://www.esphere.ru/assets/download/WebService_Comarch%20EDI.pdf
    Описание параметров:
    <::Тип_переменной -> параметр -> Описание параметра>
    ::str -> login -> ID пользователя в системе ECOD
    ::str -> password -> Пароль пользователя
    ::str -> partner_iln -> ID партнера, которому будет посылаться документ
    ::str -> document_type -> Тип документа
    ::str -> document_version -> Версия спецификации
    ::str -> document_standard -> Стандарт документа
    ::str -> document_test -> Статус документа (T – тест, P – продукционный)
    ::str -> control_number -> Контрольный номер документа
    ::str -> document_content -> Содержание документа
    ::str -> document_status -> Новый статус документа после завершения чтения документа (new(N) или read(R)).
    ::str -> date_from -> Опциональный
    ::str -> date_to -> Опциональный
    ::str -> item_from -> Опциональный
    ::str -> item_to -> Опциональный
    ::str -> control_number -> Контрольный номер документа
    ::str -> tracking_id -> Document identifier in ECOD system (in data base BTS)
    ::str -> change_document_status -> Новый статус документа после завершения чтения документа (new(N) или read(R))
    ::str -> status -> Новый статус документа
    ::str -> order_by ->
    ::int -> timeout -> Таймаут на выполнение вызова метода(мс)
    '''

    def __init__(self, url):
        session = Session()
        self.client = Client(url, transport=Transport(session=session))

    # При вызове какого либо метода, он вернет словарь с нераспарсенным xml. Это не совсем удобно для дальнейшей обработки.
    # Для этого метод возвращает из функции ParseXML расспарсенный xml.

    # Relationships метод
    # Данный метод возвращает взаимосвязи, определенные для конкретного пользователя в системе
    # ECOD. Взаимосвязи определяют с кем и какого типа документами обменивается пользователь.
    def Relationships(self, login, password, timeout):
        request_data = self.client.service.Relationships(login, password, timeout)
        return ParseRequestDataXML(request_data)

    # Send метод
    # Данный метод используется для посылки документов.
    def Send(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, control_number, document_content, timeout):
        request_data = self.client.service.Send(login, password, partner_iln, document_type, document_version, document_standard, document_test, control_number, document_content, timeout)
        return ParseRequestDataXML(request_data)

    # ListPB метод
    # Метод, позволяющий просмотреть статусы документов, пересылаемых в данный момент.
    def ListPB(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, timeout):
        request_data = self.client.service.ListPB(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, timeout)
        return ParseRequestDataXML(request_data)

    # Receive метод
    # Метод, обеспечивающий получение документов.
    def Receive(self, login, password, partner_iln, document_type, tracking_id, document_standard, change_document_status, timeout):
        request_data = self.client.service.Receive(login, password, partner_iln, document_type, tracking_id, document_standard, change_document_status, timeout)
        return ParseRequestDataXML(request_data)

    # ListMB метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMB(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, document_status, timeout):
        request_data = self.client.service.ListMB(login, password, partner_iln, document_type, document_version, document_standard, document_test, document_status, timeout)
        return ParseRequestDataXML(request_data)

    # ListMBex метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMBex(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, document_status, timeout):
        request_data = self.client.service.ListMBex(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, document_status, timeout)
        return ParseRequestDataXML(request_data)

    # ChangeDocumentStatus метод
    # Данный метод дает возможность изменить статус документа (N - new, R - read).
    def ChangeDocumentStatus(self, login, password, tracking_id, status):
        request_data = self.client.service.ChangeDocumentStatus(login, password, tracking_id, status)
        return ParseRequestDataXML(request_data)

    # ListPBEx метод
    # Метод возвращает значения статусов отосланных документов.
    def ListPBEx(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout):
<<<<<<< HEAD
        request_data = self.client.service.ListPBEx(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout)
        return ParseRequestDataXML(request_data)
=======
        return self.client.service.ListPBEx(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout)


if __name__ == "__main__":
    ss = edi_service_soap_ecod_pl("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
>>>>>>> f0da99e394518531889d196e108cb8d16fe31a1e
