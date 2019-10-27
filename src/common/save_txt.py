from typing import List, Dict
from src.common.static_method import get_no_data_value


class SaveTXT:
    def __init__(self):
        pass

    def save_to_file(self, file_path: str, contents: str) -> None:
        file_object = open(file_path, "w")
        file_object.write(contents)
        file_object.close()

    def join_by_lines(self, contents: List[str]) -> str:
        return "\n".join(contents)

    def join_by_row(self, row_contents: List[str]) -> str:
        tmp_list = self.__set_empty_cell(row_contents)

        row_out_line = ";".join(tmp_list)
        return row_out_line

    def __set_empty_cell(self, row_contents: List[str]) -> List[str]:
        return [x if x != get_no_data_value() else "" for x in row_contents]

    def convert_json_to_lines(
        self, contents: Dict[str, Dict[str, str]]
    ) -> List[List[str]]:
        data_list = []
        for _, row in contents.items():
            line_list = []
            for _, item in row.items():
                line_list.append(item)
            line_list.append("")
            data_list.append(line_list)
        return data_list
