from xml.etree import ElementTree as ET


def ParseRequestDataXML(xml):
    root = ET.fromstring(xml.Cnt)
    parse_request_data = []
    for x in range(0, len(root)):
        relation_parse = {}
        parse_request_data.append(relation_parse)
        for elem in root[x]:
            relation_parse.update({str(elem.tag): str(elem.text)})
    return parse_request_data
