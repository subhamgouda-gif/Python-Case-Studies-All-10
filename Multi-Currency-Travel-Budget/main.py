expenses = [
    ("Flights", "USD", 420, 83.0),
    ("Hotel", "EUR", 310, 90.5),
    ("Meals", "JPY", 28000, 0.56),
    ("Local travel", "USD", 95, 83.0),
    ("Activities", "EUR", 120, 90.5),
]

conversion_fee_rate = 0.02
travel_budget = 120000
category_names = []
category_totals = []
total_spending = 0

print("=" * 76)
print("MULTI-CURRENCY TRAVEL BUDGET ANALYSIS")
print("=" * 76)
print("All expenses are converted to INR using the provided sample rates.")
print("A 2% conversion fee is added to each converted expense.")
print("-" * 76)

for expense in expenses:
    category, currency, amount, exchange_rate = expense
    converted_amount = amount * exchange_rate
    conversion_fee = converted_amount * conversion_fee_rate
    total_inr = converted_amount + conversion_fee
    total_spending = total_spending + total_inr

    category_index = -1
    for index in range(len(category_names)):
        if category_names[index] == category:
            category_index = index

    if category_index == -1:
        category_names.append(category)
        category_totals.append(total_inr)
    else:
        category_totals[category_index] = category_totals[category_index] + total_inr

    print(category, "|", amount, currency, "| converted:", round(converted_amount, 2),
          "INR | fee:", round(conversion_fee, 2), "| total:", round(total_inr, 2))

largest_category = ""
largest_amount = 0
for index in range(len(category_names)):
    if category_totals[index] > largest_amount:
        largest_amount = category_totals[index]
        largest_category = category_names[index]

print("-" * 76)
print("Largest expense category:", largest_category, "|", round(largest_amount, 2), "INR")
print("Total spending:", round(total_spending, 2), "INR")
print("Budget:", travel_budget, "INR")

if total_spending > travel_budget:
    print("Budget status: OVER budget by", round(total_spending - travel_budget, 2), "INR")
else:
    print("Budget status: WITHIN budget; remaining", round(travel_budget - total_spending, 2), "INR")

print("=" * 76)
