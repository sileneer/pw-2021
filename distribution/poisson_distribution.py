import json, math, decimal

TOTAL_POP = 3837250
CHARGING_STATIONS = 94828
AVERAGE_CS_PER_CAPITA = CHARGING_STATIONS / TOTAL_POP


def poisson_distribution(u, max_of_k):
    if (u < 1):
        u = 1
    print("U: " + str(u))
    print("K: " + str(max_of_k))
    p = []
    for k in range(1, max_of_k + 1):
        power_uk = decimal.Decimal(pow(decimal.Decimal(u), decimal.Decimal(k)))
        factorial = decimal.Decimal(math.factorial(k))
        power_e = decimal.Decimal(pow(math.e, 0 - u))
        temp_p = decimal.Decimal(power_uk) // factorial * decimal.Decimal(power_e)
        p.append(float(temp_p))
    sum = 0
    for i in p:
        sum += i
    return sum


decimal.getcontext().prec = 10000

with open("cs_in_subzone.json", "r") as f:
    cs_in_subzone = json.load(f)
for item in cs_in_subzone:
    population_in_this_subzone = int(item["population"].replace(",", ""))
    poisson_distribution_result = poisson_distribution(
        round(population_in_this_subzone * AVERAGE_CS_PER_CAPITA), item["number_of_CS"])
    item["poisson"] = poisson_distribution_result

with open("cs_in_subzone.json", "w") as f:
    json.dump(cs_in_subzone, f)
