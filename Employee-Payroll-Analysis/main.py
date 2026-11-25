employees = [
    ("Mira", 42000, 12000, 2500, 12, 450, 3000),
    ("Kabir", 28000, 7000, 1800, 5, 350, 1000),
    ("Tara", 76000, 21000, 4000, 8, 600, 6000),
]

print("=" * 68)
print("EMPLOYEE PAYROLL AND DEDUCTION ANALYSIS")
print("=" * 68)
print("Tax: 5% on first 30000, 10% on next 40000, 15% above 70000.")
print("Provident fund: 8% of basic salary. Professional tax: 200.")
print("-" * 68)

for employee in employees:
    name, basic, housing, transport, overtime_hours, overtime_rate, incentive = employee
    overtime_pay = overtime_hours * overtime_rate
    gross_pay = basic + housing + transport + overtime_pay + incentive

    taxable_part = gross_pay
    if taxable_part > 30000:
        taxable_part = 30000
    tax = taxable_part * 0.05

    if gross_pay > 30000:
        taxable_part = gross_pay - 30000
        if taxable_part > 40000:
            taxable_part = 40000
        tax = tax + taxable_part * 0.10

    if gross_pay > 70000:
        taxable_part = gross_pay - 70000
        tax = tax + taxable_part * 0.15

    provident_fund = basic * 0.08
    professional_tax = 200
    total_deductions = tax + provident_fund + professional_tax
    net_pay = gross_pay - total_deductions

    print("EMPLOYEE:", name)
    print("  Basic:", basic, "| allowances:", housing + transport,
          "| overtime:", overtime_pay, "| incentive:", incentive)
    print("  Gross:", round(gross_pay, 2), "| income tax:", round(tax, 2),
          "| provident fund:", round(provident_fund, 2),
          "| professional tax:", professional_tax)
    print("  Total deductions:", round(total_deductions, 2),
          "| NET PAY:", round(net_pay, 2))
    print("-" * 68)

print("=" * 68)
