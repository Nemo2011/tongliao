import json
from pprint import pprint
from .core import area2tongliao, people2tongliao

DATA = json.load(open("countries_data.json", "r", encoding = "utf-8"))

def country2tongliao(country):
    if not country in DATA.keys():
        return {}
    return {
        "name": country, 
        "area": DATA[country]["area"], 
        "people": DATA[country]["people"], 
        "area_str": str(DATA[country]["area"]) + " 平方千米(km²)", 
        "people_str": str(DATA[country]["people"]) + " 人", 
        "result": {
            "area": round(area2tongliao(DATA[country]["area"]), 2), 
            "people": round(people2tongliao(DATA[country]["people"]), 2), 
            "area_str": str(round(area2tongliao(DATA[country]["area"]), 2)) + " 通辽(T)",
            "people_str": str(round(people2tongliao(DATA[country]["people"]), 2)) + " 通辽(T)"
        }
    }

if __name__ == "__main__":
    pprint(country2tongliao("中国"))
