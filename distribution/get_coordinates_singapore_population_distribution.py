from openpyxl import load_workbook
import urllib, json
import requests

workbook = load_workbook(filename="singapore_population_distribution.xlsx")
sheet = workbook.active
location_names = []
for a in sheet["A"]:
    if a.value is not None:
        location_names.append(a.value)
del (location_names[0])
print(location_names)

i = 2
for location_name in location_names:
    url = "https://nominatim.openstreetmap.org/search?q=" + location_name + " Singapore" + "&format=json"
    response = requests.get(url)
    print(response.json())
    try:
        response_json = response.json()
        lat = response_json[0]["lat"]
        lon = response_json[0]["lon"]

        sheet["C" + str(i)] = lat
        sheet["D" + str(i)] = lon
    except:
        print("***** location not found *****")

    i += 1

workbook.save("result_singapore_population_distribution.xlsx")
