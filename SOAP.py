# Created: 02.05.2020 9:12
# Language: Python 3.6.5
# Version: 1.0
# Author: Orlov Alexandr
# Documentation: https://www.esphere.ru/assets/download/WebService_Comarch%20EDI.pdf


import os
from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.exceptions import ConnectTimeout


class get_key_client:
    def __init__(self, key):
        self.key = key

    def __get__(self, instance, owner):
        return instance.__dict__[self.key]

    def __set__(self, instance, value):
        if value == "login":
            return os.getenv("NAME_KEY")
        elif value == "password":
            return os.getenv("PASSWORD_KEY")


class edi_service_soap_ecod_pl():
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

    # Relationships метод
    # Данный метод возвращает взаимосвязи, определенные для конкретного пользователя в системе
    # ECOD. Взаимосвязи определяют с кем и какого типа документами обменивается пользователь.
    def Relationships(self, login, password, timeout):
        return self.client.service.Relationships(login, password, timeout)

    # Send метод
    # Данный метод используется для посылки документов.
    def Send(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, control_number, document_content, timeout):
        return self.client.service.Send(login, password, partner_iln, document_type, document_version, document_standard, document_test, control_number, document_content, timeout)

    # ListPB метод
    # Метод, позволяющий просмотреть статусы документов, пересылаемых в данный момент.
    def ListPB(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, timeout):
        return self.client.service.ListPB(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, timeout)

    # Receive метод
    # Метод, обеспечивающий получение документов.
    def Receive(self, login, password, partner_iln, document_type, tracking_id, document_standard, change_document_status, timeout):
        return self.client.service.Receive(login, password, partner_iln, document_type, tracking_id, document_standard, change_document_status, timeout)

    # ListMB метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMB(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, document_status, timeout):
        return self.client.service.ListMB(login, password, partner_iln, document_type, document_version, document_standard, document_test, document_status, timeout)

    # ListMBex метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMBex(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, document_status, timeout):
        return self.client.service.ListMBex(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, document_status, timeout)

    # ChangeDocumentStatus метод
    # Данный метод дает возможность изменить статус документа (N - new, R - read).
    def ChangeDocumentStatus(self, login, password, tracking_id, status):
        return self.client.service.ChangeDocumentStatus(login, password, tracking_id, status)

    # ListPBEx метод
    # Метод возвращает значения статусов отосланных документов.
    def ListPBEx(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout):
        return self.client.service.ListPBEx(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout)


if __name__ == "__main__":
    try:
        SOAPClient = edi_service_soap_ecod_pl("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
    except ConnectTimeout:
        try:
            SOAPClient = edi_service_soap_ecod_pl("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
        except ConnectTimeout:
            try:
                SOAPClient = edi_service_soap_ecod_pl("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL")
            except ConnectTimeout:
                raise
    else:
        print(SOAPClient.Relationships(get_key_client('login'), get_key_client('password'), 1000))
        #print(SOAPClient.Send(get_key_client('login'), get_key_client('password'), "2000000000009", "INVOICE", "ECODV0R1", "XML", "T", "", "test", 5000))
        #print(SOAPClient.ListPB(get_key_client('login'), get_key_client('password'), "2000000000009", "INVOICE", "ECODV0R2", "EDIFACT", "T", "2002-09-11", "2002-09-10", "", "", 10000))
        #print(SOAPClient.Receive(get_key_client('login'), get_key_client('password'), "2000000000009", "INVOICE", "{D1BA990B-98A6-40AE-B7F0-29A240CB54F0}", "XML", "R", 10000))
        #print(SOAPClient.ListMB(get_key_client('login'), get_key_client('password'), "2000000000009", "INVOICE", "ECODV0R2", "XML", "T", "A", 10000))
        # print(SOAPClient.ListMBex(get_key_client('login'), get_key_client('password'), "2000000000009", "INVOICE", "ECODV0R1", "XML", "T", "2002-09-11", "2002-09-10", "", "", "N", 5000))
        #print(SOAPClient.ChangeDocumentStatus(get_key_client('login'), get_key_client('password'), "{57100E2A-ABE3-4DF5B61D-1C673C86DACD}", "R"))
        #print(SOAPClient.ListPBEx(get_key_client('login'), get_key_client('password'), "2000000000009", "INVOICE", "ECODV0R2", "XML", "T", "2002-09-11", "2002-09-10", "", "", "", 5000))
        # code is here...
