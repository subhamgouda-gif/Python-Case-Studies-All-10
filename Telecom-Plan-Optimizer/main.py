plans = [
    ("Starter", 249, 28, 8, 25),
    ("Everyday", 399, 56, 20, 20),
    ("Power", 599, 84, 40, 15),
    ("Max", 799, 84, 80, 10),
]

subscribers = [
    ("Aman", 15, 28, 450),
    ("Leena", 36, 56, 650),
    ("Rohan", 74, 84, 850),
    ("Isha", 10, 90, 500),
]

print("=" * 68)
print("MULTI-PLAN TELECOMMUNICATION COST OPTIMIZER")
print("=" * 68)
print("Excess data is charged per GB. A plan must cover validity and budget.")
print("-" * 68)

for subscriber in subscribers:
    name, data_used, days_needed, budget = subscriber
    best_plan = None
    best_cost = 0

    print(name, "| usage:", data_used, "GB | days:", days_needed,
          "| budget:", budget)

    for plan in plans:
        plan_name, base_price, validity_days, included_data, excess_rate = plan

        if data_used > included_data:
            excess_data = data_used - included_data
        else:
            excess_data = 0

        total_cost = base_price + excess_data * excess_rate

        if validity_days >= days_needed and total_cost <= budget:
            if best_plan is None or total_cost < best_cost:
                best_plan = plan
                best_cost = total_cost
            elif total_cost == best_cost and validity_days > best_plan[2]:
                best_plan = plan
                best_cost = total_cost

    if best_plan is None:
        print("  No available plan meets both validity and budget.")
    else:
        plan_name, base_price, validity_days, included_data, excess_rate = best_plan
        if data_used > included_data:
            excess_data = data_used - included_data
        else:
            excess_data = 0
        print("  Recommended:", plan_name, "| base:", base_price,
              "| excess charge:", round(excess_data * excess_rate, 2),
              "| total:", round(best_cost, 2))
    print("-" * 68)

print("=" * 68)
