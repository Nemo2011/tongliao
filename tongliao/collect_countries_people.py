from bs4 import BeautifulSoup
import requests
import json

def collect_countries_people():
    page = 1

    json_data = {

    }

    cnt = 0
    for _ in range(12):
        resp = requests.get(f"https://mip.phb123.com/city/renkou/rk_{page}.html")
        resp.raise_for_status()

        soup = BeautifulSoup(resp.text, "lxml")
        for child in (soup.body
            .findChildren("div")[5]
            .findChildren("table")[0]
            .findChildren("tbody")[0]
            .findChildren("tr")[1:]):
            tds = child.findChildren("td")
            name = tds[1].findChildren("a")[0].findChildren("p")[0].string
            people = int(tds[2].string.replace(",", ""))
            json_data[name] = people
            cnt += 1
            print("人口数据载入已完成: " + str(round(cnt / 238 * 100, 2)) + "%\r", end = "")

        page += 1

    json.dump(json_data, open("countries_people_data.json", "w+", encoding = "utf-8"), indent = 4, ensure_ascii = False)

    print()
