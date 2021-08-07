import math

import geojson, json

with open("ura-parking-lot-geojson.geojson") as f:
    carpark_geojson_file = geojson.load(f)

carpark_origin_data = carpark_geojson_file["features"]
stage_1_results = []
stage_2_results = []


def get_coordinates(para_coordinates):
    sum_x = 0
    sum_y = 0
    count = 0
    for item in para_coordinates:
        sum_x += item[0]
        sum_y += item[1]
        count += 1
    return [sum_x / count, sum_y / count]


def get_name(str):
    index_start = str.find("PARKING_PL") + 20
    index_end = index_start + str[index_start:].find("</td>")
    return str[index_start:index_end]


# result format: [{'name': 'BOON LAY WAY HVP', 'coordinates': [103.751429, 1.3267396]}, ...]
def stage_1():
    for item in carpark_origin_data:
        result = {
            "name": get_name(item["properties"]["Description"]).strip(),
            "coordinates": get_coordinates(item["geometry"]["coordinates"][0])
        }
        stage_1_results.append(result)
    return stage_1_results


# merge the repeated data
def stage_2():
    names_storage = []
    for item in stage_1_results:
        name = item["name"]
        coordinates = item["coordinates"]
        if name not in names_storage:
            names_storage.append(name)
        else:
            pass
    for name in names_storage:
        temp_coordinates = []
        count = 0
        for item in stage_1_results:
            if item["name"] == name:
                temp_coordinates.append(item["coordinates"])
                count += 1
        sum_x = 0
        sum_y = 0
        for item in temp_coordinates:
            sum_x += item[0]
            sum_y += item[1]
        result = {"name": name, "coordinates": [sum_x / count, sum_y / count], "count": count}
        stage_2_results.append(result)
    return stage_2_results


stage_1()
stage_2()


def get_number_of_cs(number_of_parking_lots):
    if number_of_parking_lots <= 3:
        return 1
    else:
        return round(number_of_parking_lots * 0.31)


count_number_of_charging_stations = 0
for item in stage_2_results:
    item["latitude"] = item["coordinates"][1]
    item["longitude"] = item["coordinates"][0]
    number_of_charging_station = get_number_of_cs(item["count"])
    count_number_of_charging_stations += number_of_charging_station
    item["number_of_charging_station"] = number_of_charging_station
print(count_number_of_charging_stations)

with open('carpark_distribution.json', 'w') as f:
    json.dump(stage_2_results, f)
