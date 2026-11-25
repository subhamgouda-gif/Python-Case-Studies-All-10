monthly_usage = [
    ("July", 84),
    ("August", 110),
    ("September", 128),
    ("October", 312),
    ("November", 305),
]

slabs = [(100, 4.5), (100, 6.0), (999999, 8.0)]
fixed_charge = 75
high_use_limit = 250
surcharge_rate = 0.05
low_use_limit = 100
low_use_rebate = 25
previous_bill = 0

print("=" * 68)
print("PROGRESSIVE ELECTRICITY BILLING")
print("=" * 68)
print("Rates: first 100 units at 4.50, next 100 at 6.00, remaining at 8.00.")
print("A 5% surcharge applies above 250 units; use up to 100 gets 25 rebate.")
print("-" * 68)

for month_record in monthly_usage:
    month, units = month_record
    remaining_units = units
    energy_charge = 0

    for slab_units, rate in slabs:
        if remaining_units > 0:
            if remaining_units < slab_units:
                charged_units = remaining_units
            else:
                charged_units = slab_units
            energy_charge = energy_charge + charged_units * rate
            remaining_units = remaining_units - charged_units

    surcharge = 0
    if units > high_use_limit:
        surcharge = energy_charge * surcharge_rate

    rebate = 0
    if units <= low_use_limit:
        rebate = low_use_rebate

    bill = energy_charge + fixed_charge + surcharge - rebate
    print(month, "- units:", units, "| energy:", round(energy_charge, 2),
          "| surcharge:", round(surcharge, 2), "| rebate:", rebate,
          "| total:", round(bill, 2))

    if previous_bill > 0 and bill > previous_bill * 1.30:
        print("  ALERT: bill increased by more than 30% from the previous month.")

    previous_bill = bill

print("=" * 68)
