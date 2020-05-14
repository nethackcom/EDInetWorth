from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from SOAP import edi_service_soap_ecod_pl
import os


class my_data_base(edi_service_soap_ecod_pl):
    def __init__(self, wsdl_url, DB_ENGINE):
        super(my_data_base, self).__init__(wsdl_url)
        self.engine = create_engine(DB_ENGINE, echo=True)

        self.argument_request_relationships = [
            "relation_id",  # Идентификатор взаимосвязи
            "partner_iln",  # ID партнера, с которым определена взаимосвязь
            "direction",  # IN или OUT. Получен или отправлен
            "document_type",  # Тип документа
            "document_version",  # Версия спецификации
            "document_test",  # Стандарт документа
            "description",  # Описание взаимосвязи
            "test"  # Статус документа
        ]

    def execute_query(self, query=''):
        if query == '': return
        print(query)

        with self.engine.connect() as connection:
            try:
                connection.execute(query)
            except Exception as e:
                print(e)

    def create_tables_relationships(self):
        meta = MetaData()
        requests_relationships_in = Table(
            'Table_from_requests_relationships_in', meta,
            Column('Name_of_field', String, primary_key=True),
            Column('Content_request', String)
        )
        requests_relationships_out = Table(
            'Table_from_requests_relationships_out', meta,
            Column('Name_of_field', String, primary_key=True),
            Column('Content_request', String)
        )
        return meta.create_all(self.engine)

    # Update
    def data_update(self):
        st = edi_service_soap_ecod_pl.Relationships(self, os.getenv("NAME_KEY"), os.getenv("PASSWORD_KEY"), 5000)
        for argument in self.argument_request_relationships:
            conn = self.engine.connect()
            query = "UPDATE Table_from_requests_relationships_in SET Content_request='' WHERE Name_of_field='{argument}'".format(argument=argument)
            conn.execute(query)
            conn.close()


if __name__ == "__main__":
    db = my_data_base("https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL", "sqlite:///request_of_methods.db")
    db.create_tables_relationships()
    db.data_update()