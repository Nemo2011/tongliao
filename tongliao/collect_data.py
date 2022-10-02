import json
from .collect_countries_area import collect_countries_area
from .collect_countries_people import collect_countries_people

def collect_data():
    collect_countries_people()
    collect_countries_area()
    area_data = json.load(open("countries_area_data.json", encoding = "utf-8"))
    people_data = json.load(open("countries_people_data.json", encoding = "utf-8"))

    json_data = {

    }

    for name, area in area_data.items():
        if name in people_data.keys():
            people = people_data[name]
            json_data[name] = {
                "area": area, 
                "people": people
            }

    json.dump(json_data, open("countries_data.json", "w+", encoding = "utf-8"), indent = 4, ensure_ascii = False)
