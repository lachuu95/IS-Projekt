from typing import List, Dict
from src.common.constants import no_data_value


class ReadTXT:
    def __init__(self, column_name: List[str]):
        self.__column_name = column_name

    def read_from_file(self, file_path: str) -> str:
        file_object = open(file_path, "r")
        file_contents = file_object.read()
        file_object.close()
        return file_contents

    def split_by_lines(self, contents: str) -> List[str]:
        return contents.splitlines()

    def split_by_row(self, row_contents: str) -> List[str]:
        row_in_list = row_contents.split(";")
        return self.__fill_empty_cell(row_in_list)

    def __fill_empty_cell(self, row_contents: List[str]) -> List[str]:
        return [x if x != "" else no_data_value() for x in row_contents]

    def convert_lines_to_json(
        self, contents: List[List[str]]
    ) -> Dict[str, Dict[str, str]]:
        data_dict = {}
        for row_index, row in enumerate(contents, start=1):
            del row[-1]
            data_dict[str(row_index)] = {
                self.__column_name[item_index]: item
                for item_index, item in enumerate(row)
            }
        return data_dict
