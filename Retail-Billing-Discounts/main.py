products = [
    ("T-shirt", "Clothing", 800, 3),
    ("Water bottle", "Accessories", 450, 2),
    ("Running shoes", "Footwear", 3200, 1),
]

category_taxes = [
    ("Clothing", 0.05),
    ("Accessories", 0.12),
    ("Footwear", 0.18),
]

line_grosses = []
line_bulk_discounts = []
line_net_before_order = []
line_tax_rates = []
gross_total = 0
bulk_discount_total = 0

for product in products:
    name, category, price, quantity = product
    line_gross = price * quantity
    gross_total = gross_total + line_gross

    if quantity >= 3:
        bulk_discount = line_gross * 0.05
    else:
        bulk_discount = 0

    tax_rate = 0
    for tax_record in category_taxes:
        tax_category, tax_value = tax_record
        if tax_category == category:
            tax_rate = tax_value

    line_grosses.append(line_gross)
    line_bulk_discounts.append(bulk_discount)
    line_net_before_order.append(line_gross - bulk_discount)
    line_tax_rates.append(tax_rate)
    bulk_discount_total = bulk_discount_total + bulk_discount

after_bulk_total = gross_total - bulk_discount_total
order_discount = 0
if gross_total >= 5000:
    order_discount = after_bulk_total * 0.10

maximum_discount = gross_total * 0.20
if bulk_discount_total + order_discount > maximum_discount:
    order_discount = maximum_discount - bulk_discount_total

print("=" * 76)
print("RETAIL BILLING WITH MULTIPLE DISCOUNT RULES")
print("=" * 76)
print("Bulk rule: 5% for quantity >= 3. Order rule: 10% when gross >= 5000.")
print("Total discount cap: 20% of gross. Category tax is applied after discounts.")
print("-" * 76)
print("Item | Quantity | Gross | Bulk discount | Order discount | Tax | Line total")

tax_total = 0
final_total = 0
for index in range(len(products)):
    name, category, price, quantity = products[index]
    allocated_order_discount = 0
    if after_bulk_total > 0:
        allocated_order_discount = (
            order_discount * line_net_before_order[index] / after_bulk_total
        )

    taxable_amount = line_net_before_order[index] - allocated_order_discount
    item_tax = taxable_amount * line_tax_rates[index]
    line_total = taxable_amount + item_tax
    tax_total = tax_total + item_tax
    final_total = final_total + line_total

    print(name, "|", quantity, "|", round(line_grosses[index], 2),
          "|", round(line_bulk_discounts[index], 2),
          "|", round(allocated_order_discount, 2),
          "|", round(item_tax, 2), "|", round(line_total, 2))

print("-" * 76)
print("Gross:", round(gross_total, 2),
      "| total discount:", round(bulk_discount_total + order_discount, 2),
      "| tax:", round(tax_total, 2),
      "| AMOUNT DUE:", round(final_total, 2))
print("=" * 76)
