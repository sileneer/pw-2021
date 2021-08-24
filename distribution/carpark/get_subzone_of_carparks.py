import json, math

with open("../population/cs_and_population_distribution.json") as f:
    population_distribution = json.load(f)

with open("cs_and_carpark_distribution.json") as f:
    carpark_distribution = json.load(f)

subzone_data = []
for item in population_distribution:
    data = {"label": item["label"], "latitude": item["latitude"], "longitude": item["longitude"]}
    subzone_data.append(data)


for carpark in carpark_distribution:
    temp_name_of_subzone = ""
    min_distance = 100000
    for subzone in subzone_data:
        distance = math.sqrt(
            math.pow((float(carpark["latitude"]) - float(subzone["latitude"])), 2) +
            math.pow((float(carpark["longitude"]) - float(subzone["longitude"])), 2))
        if distance < min_distance:
            min_distance = distance
            temp_name_of_subzone = subzone["label"]
    carpark["subzone"] = temp_name_of_subzone


with open('cs_and_carpark_distribution.json', 'w') as f:
    json.dump(carpark_distribution, f)