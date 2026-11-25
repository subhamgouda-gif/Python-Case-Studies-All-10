products = [
    ("Desk", 40, 1800, 650, 12000, 0.06, 4200, 0.20),
    ("Chair", 75, 900, 400, 15000, 0.04, 2100, 0.18),
    ("Shelf", 25, 2400, 800, 9000, 0.08, 4300, 0.22),
]

print("=" * 76)
print("MANUFACTURING COST AND PROFITABILITY ANALYSIS")
print("=" * 76)
print("Material wastage is calculated as a percentage of material cost.")
print("Target profit rate is profit divided by total production cost.")
print("-" * 76)

for product in products:
    name, units, material_per_unit, labor_per_unit, machine_cost, wastage_rate, selling_price, target_rate = product

    material_cost = units * material_per_unit
    wastage_cost = material_cost * wastage_rate
    labor_cost = units * labor_per_unit
    total_cost = material_cost + wastage_cost + labor_cost + machine_cost
    revenue = units * selling_price
    profit = revenue - total_cost

    if total_cost > 0:
        profit_rate = profit / total_cost
    else:
        profit_rate = 0

    if profit_rate >= target_rate:
        target_status = "TARGET MET"
    else:
        target_status = "TARGET NOT MET"

    print(name, "| units:", units)
    print("  Material:", round(material_cost, 2),
          "| wastage:", round(wastage_cost, 2),
          "| labor:", round(labor_cost, 2),
          "| machine:", round(machine_cost, 2))
    print("  Total cost:", round(total_cost, 2),
          "| revenue:", round(revenue, 2),
          "| profit:", round(profit, 2),
          "| profit rate:", round(profit_rate * 100, 2), "%",
          "|", target_status)
    print("-" * 76)

print("=" * 76)
