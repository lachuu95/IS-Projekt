#!/usr/bin/env python3
from zeep import Client
import json

client = Client("http://localhost:58585/SelectFromDB/soap/description?WSDL")

try:
    result = client.service.get_screen_type()
    print(result)
except:
    print("nie działa")

try:
    result = client.service.get_manufacturer()
    print(result)
except:
    print("nie działa")

try:
    result = client.service.count_manufacturer("Dell")
    print(result)
except:
    print("nie działa")

try:
    result = client.service.get_screen_type_data("matowa")
    print(json.loads(result))
except:
    print("nie działa")
