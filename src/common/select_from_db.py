from ladon.ladonizer import ladonize
import json
import os
import sys

sys.path.append(os.path.dirname(os.path.dirname(sys.path[0])))
from src.common.dataset import Dataset

class SelectFromDB(object):

    @ladonize(rtype=[str])
    def get_manufacturer(self):
        data = Dataset()
        return data.get_unique_list_from_db(data.columns_headers[0])

    @ladonize(rtype=[str])
    def get_screen_type(self):
        data = Dataset()
        return data.get_unique_list_from_db(data.columns_headers[3])

    @ladonize(str, rtype=int)
    def count_manufacturer(self, msg):
        data = Dataset()
        data.get_all_where_from_db(data.columns_headers[0], msg)
        return len(data.data)

    @ladonize(str, rtype=str)
    def get_screen_type_data(self, msg):
        data = Dataset()
        data.get_all_where_from_db(data.columns_headers[3], msg)
        return str(json.dumps(data.data))