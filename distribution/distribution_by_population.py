import json

REMAINING_CHARGING_STATIONS = 94828 - 13083
TOTAL_POP = 3837250
EV_PER_CAPITA = REMAINING_CHARGING_STATIONS / TOTAL_POP

with open("population_distribution.json") as f:
    population_distribution = json.load(f)

for item in population_distribution:
    item["latitude"] = float(item["latitude"])
    item["longitude"] = float(item["longitude"])
    number_of_CS = round(float(item["population"].replace(',', '')) * EV_PER_CAPITA)
    if number_of_CS ==0:
        item["number_of_CS"] = 1
    else:
        item["number_of_CS"] = number_of_CS
with open('population_distribution.json', 'w') as f:
    json.dump(population_distribution, f)
