from xml.etree import ElementTree as ET
from typing import Dict
import collections 
from src.common.constants import no_data_value,translate_headers_xls_to_name

class ReadXML():
    def __init__(self):
        pass

    def read_from_xml_to_json(self, file_path: str) -> Dict[str,Dict[str,str]]:
        tree = ET.parse(file_path)
        root = tree.getroot()
        translate_dict = translate_headers_xls_to_name()
        data_dict = {}
        for child in root:
            data_dict[str(child.attrib["id"])] = {}
            for x in child:
                if len(x)==0:
                    data_dict[str(child.attrib["id"])][translate_dict[str(x.tag)]] = x.text if not((x.text is None) or (x.text == "")) else no_data_value()
                else:
                    for y in x:
                        data_dict[str(child.attrib["id"])][translate_dict[str(x.tag+" "+y.tag)]] = y.text if not((y.text is None) or (y.text == "")) else no_data_value()
        return data_dict
