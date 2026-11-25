patients = [
    ("Nila", 500, 1400, 6200, 66, 180000, 5000),
    ("Arun", 500, 900, 3800, 34, 420000, 5200),
    ("Kiran", 600, 1600, 8000, 48, 150000, 3000),
    ("Sana", 450, 700, 2500, 27, 300000, 6000),
]

print("=" * 68)
print("HOSPITAL BILLING AND PATIENT CLASSIFICATION")
print("=" * 68)
print("Concessions: 10% for age 60+, plus 5% for income up to 200000.")
print("Payment status: fully paid, partial payment (at least 50%), or balance due.")
print("-" * 68)

for patient in patients:
    name, consultation, diagnostics, treatment, age, income, amount_paid = patient
    charges_are_valid = True

    for charge in (consultation, diagnostics, treatment):
        if charge < 0:
            charges_are_valid = False
    if age < 0 or income < 0 or amount_paid < 0:
        charges_are_valid = False

    if not charges_are_valid:
        print(name, "- INVALID: negative age, income, payment, or charge.")
    else:
        gross_bill = consultation + diagnostics + treatment
        concession_rate = 0

        if age >= 60:
            concession_rate = concession_rate + 0.10
        if income <= 200000:
            concession_rate = concession_rate + 0.05
        if concession_rate > 0.15:
            concession_rate = 0.15

        concession = gross_bill * concession_rate
        final_bill = gross_bill - concession

        if amount_paid > final_bill:
            print(name, "- INVALID: payment exceeds the final bill.")
        else:
            balance = final_bill - amount_paid

            if amount_paid == final_bill:
                status = "FULLY PAID"
            elif amount_paid >= final_bill * 0.50:
                status = "PARTIAL PAYMENT"
            else:
                status = "BALANCE DUE"

            print(name, "| gross:", round(gross_bill, 2),
                  "| concession:", round(concession, 2),
                  "| final bill:", round(final_bill, 2),
                  "| paid:", round(amount_paid, 2),
                  "| balance:", round(balance, 2),
                  "| status:", status)

print("=" * 68)
