from xml.etree import ElementTree as ET
from xml.etree.ElementTree import ParseError
from Edi_Service_Soap_Ecod_Pl import EdiServiceSoapEcodPl


class EdiService(EdiServiceSoapEcodPl):

    ''' Класс EdiService предназначен для парсинга данных из вызовов родительских методов.
    В этом классе все методы родителя переопределенны.
    '''

    def ParseXML(self, xml):
        ''' Метод ParseXML реализован следующим образом.

        Метод на входе принимает request data из методов родительского класса. После чего берет XML строку и начинает парсить ее.
        Каждый XML документ лежит в своем теге. Метод парсит каждый документ и заносит данные документа в словарь.
        После чего словарь помещается в массив document_data.
        На выходе метод ParseXML возвращает массив со всеми распарсенными документами.

        При пустом документе будет возвращать False.

        *documents_data* хранит в себе все распарсенные документы
        *document* хранит в себе один распарсенный документ
        *document_content* хранит в себе содержание нераспарсенного документа
        '''
        documents_data = []
        document_content = xml.Cnt
        try:
            if document_content == None:
                return False
            else:
                root = ET.fromstring(document_content)
                for x in range(0, len(root)):
                    document = {}
                    documents_data.append(document)
                    for elem in root[x]:
                        document.update({str(elem.tag): elem.text})
                return documents_data
        except ParseError:
            # Используем исключение в том случае, если значение возвращаемое в словаре с ключем 'Cnt' не нужно парсить.
            documents_data.append(xml.Cnt)
            return documents_data

    def Relationships(self, login, password, timeout):
        request_data = super().Relationships(login, password, timeout)
        return self.ParseXML(request_data)

    # Send метод
    # Данный метод используется для посылки документов.
    def Send(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, control_number, document_content, timeout):
        request_data = super().Send(login, password, partner_iln, document_type, document_version, document_standard, document_test, control_number, document_content, timeout)
        return self.ParseXML(request_data)

    # ListPB метод
    # Метод, позволяющий просмотреть статусы документов, пересылаемых в данный момент.
    def ListPB(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, timeout):
        request_data = super().ListPB(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, timeout)
        return self.ParseXML(request_data)

    # Receive метод
    # Метод, обеспечивающий получение документов.
    def Receive(self, login, password, partner_iln, document_type, tracking_id, document_standard, change_document_status, timeout):
        request_data = super().Receive(login, password, partner_iln, document_type, tracking_id, document_standard, change_document_status, timeout)
        return self.ParseXML(request_data)

    # ListMB метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMB(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, document_status, timeout):
        request_data = super().ListMB(login, password, partner_iln, document_type, document_version, document_standard, document_test, document_status, timeout)
        return self.ParseXML(request_data)

    # ListMBex метод
    # Метод возвращает статус документов, которые были доставлены пользователю ECOD.
    def ListMBex(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, document_status, timeout):
        request_data = super().ListMBex(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, document_status, timeout)
        return self.ParseXML(request_data)

    # ChangeDocumentStatus метод
    # Данный метод дает возможность изменить статус документа (N - new, R - read).
    def ChangeDocumentStatus(self, login, password, tracking_id, status):
        request_data = super().ChangeDocumentStatus(login, password, tracking_id, status)
        return self.ParseXML(request_data)

    # ListPBEx метод
    # Метод возвращает значения статусов отосланных документов.
    def ListPBEx(self, login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout):
        request_data = super().ListPBEx(login, password, partner_iln, document_type, document_version, document_standard, document_test, date_from, date_to, item_from, item_to, order_by, timeout)
        return self.ParseXML(request_data)