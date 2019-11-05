import xml.etree.cElementTree as ET
from datetime import datetime
from src.common.constants import translate_headers_name_to_xls,no_data_value

class SaveXML():
    def __init__(self):
        self.__data_dict = None


    def translate_data(self, data_dict):
        translate_dict = translate_headers_name_to_xls()
        new_dict={}
        for idx, values in data_dict.items():
            new_dict[idx]={}
            for key, item in values.items():
                xml_name = translate_dict[key]
                xml_name_list = xml_name.split()
                item_to_write = item if item != no_data_value() else None
                if not xml_name_list[0] in new_dict[idx]:
                    new_dict[idx][xml_name_list[0]] = {}
                if len(xml_name_list) !=1 :
                    new_dict[idx][xml_name_list[0]][xml_name_list[1]]=item_to_write
                else:
                    new_dict[idx][xml_name_list[0]]=item_to_write
        self.__data_dict = new_dict
    
    def save_xml(self, file_path: str) -> None:
        root = ET.Element("laptops",{'moddate': datetime.now().strftime("%Y-%m-%d %a %H:%M")})
        root.text = "\n\t"
        root.tail = "\n\t"
        for idx, values in self.__data_dict.items():
            child = ET.SubElement(root, "laptop",{"id":idx})
            child.text = "\n\t\t"
            child.tail = "\n\t"
            for key, item in values.items():
                tmp_xml_item = ET.SubElement(child, key)
                tmp_xml_item.text = "\n\t\t\t"
                tmp_xml_item.tail = "\n\t\t"
                if type(item) is dict:
                    for subkey, subitem in item.items():
                        tmp_xml_subitem = ET.SubElement(tmp_xml_item, subkey)
                        tmp_xml_subitem.text = subitem
                        tmp_xml_subitem.tail = "\n\t\t\t"
                    tmp_xml_subitem.tail = "\n\t\t"
                else:
                    tmp_xml_item.text = item
                    tmp_xml_item.tail = "\n\t\t"
            tmp_xml_item.tail = "\n\t"
        child.tail = "\n"
        tree = ET.ElementTree(root)
        tree.write(file_path, xml_declaration=True, encoding="UTF-8")
