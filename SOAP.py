# Created 02.05.2020 9:12
# Version 1.0
# Copyright Orlov Alexandr

from zeep import Client
from zeep.transports import Transport
from requests import Session
from requests.auth import HTTPBasicAuth


class SOAP(object):
    def __init__(self):
        pass

    def client(self, url, data):
        wsdl = url
        session = Session()
        session.auth = HTTPBasicAuth(data["Name"], data["Password"])
        client = Client(wsdl, transport=Transport(session=session))
        request_data = data
        response = client.service.Relationships(**request_data)
        print(client)
        print(session.auth)
        print(response)


if __name__ == "__main__":
    SOAP = SOAP()
    SOAP.client(
        "https://www.ecod.pl/webserv2/EDIservice.asmx?WSDL",
        {
            "Name": "name",
            "Password": "password",
            "Timeout": 5000
        }
    )