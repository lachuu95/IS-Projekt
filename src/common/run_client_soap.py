from zeep import Client
import json

#TODO: Autowyszukiwanie w sieci lokalnej, okno klienta, uruchamianie serwera.
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
