import json

results = []
with open('population/cs_and_population_distribution.json', 'r') as f:
    population_distribution = json.load(f)

for item in population_distribution:
    result = {
        "name": item["label"],
        "population": item["population"],
        "number_of_CS": item["number_of_CS"],
        "latitude": item["latitude"],
        "longitude": item["longitude"]
    }
    results.append(result)

with open('carpark/cs_and_carpark_distribution.json', 'r') as f:
    carpark_distribution = json.load(f)
for item in carpark_distribution:
    subzone_name = item["subzone"]
    for result in results:
        if subzone_name == result["name"]:
            result["number_of_CS"] += item["number_of_charging_station"]

print(results)
with open('cs_in_subzone.json', 'w') as f:
    json.dump(results, f)
