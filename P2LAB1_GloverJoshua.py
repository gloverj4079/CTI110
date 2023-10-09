mileage = float(input())
gas_cost = float(input())
miles = 20
miles2 = 75
miles3 = 500
gas_cost_25_miles = (miles/mileage) * gas_cost
gas_cost_75_miles = (miles2/mileage) * gas_cost
gas_cost_500_miles = (miles3/mileage) * gas_cost
print(f"{gas_cost_25_miles:.2f} {gas_cost_75_miles:.2f} {gas_cost_500_miles:.2f}")

