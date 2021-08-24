import json

with open("new_york_state_ev.json") as f:
    new_york_state = json.load(f)

ev_in_new_york = new_york_state["fuel_stations"]
results = []

for i in ev_in_new_york:
    print(i["city"])
    if i["city"].lower() in ["new york", "queens", "bronx", "brooklyn", "manhattan", "staten island"]:
        results.append(i)

with open('new_york_city_ev.json', 'w') as json_file:
    json.dump(results, json_file)
