import json

REMAINING_CHARGING_STATIONS = 94828 - 8440
TOTAL_POP = 3837250
EV_PER_CAPITA = REMAINING_CHARGING_STATIONS / TOTAL_POP

with open("population_distribution.json") as f:
    population_distribution = json.load(f)

for item in population_distribution:
    item["latitude"] = float(item["latitude"])
    item["longitude"] = float(item["longitude"])
    item["number_of_CS"] = round(float(item["population"].replace(',', '')) * EV_PER_CAPITA)

with open('population_distribution.json', 'w') as f:
    json.dump(population_distribution, f)
