from openpyxl import Workbook
import requests

workbook = Workbook()
petrol_station_brand = ["Shell", "SPC", "Esso", "Caltex"]
for name in petrol_station_brand:
    workbook.create_sheet(name)
    sheet = workbook[name]
    sheet["A1"] = "name"
    sheet["B1"] = "latitude"
    sheet["C1"] = "longitude"
    url = "https://nominatim.openstreetmap.org/search?q=" + name + "&format=json&limit=100&countrycodes=sg"
    response = requests.get(url)
    response_json = response.json()
    i = 2
    for item in response_json:
        print(item)
        name = item["display_name"]
        lat = item["lat"]
        lon = item["lon"]
        sheet["A" + str(i)] = name
        sheet["B" + str(i)] = lat
        sheet["C" + str(i)] = lon
        i += 1

workbook.save("result_singapore_petrol_station.xlsx")
