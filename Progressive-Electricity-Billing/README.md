# Progressive Electricity Billing

Calculates a monthly electricity bill using consumption slabs, a fixed charge, a high-use surcharge, and a low-use rebate. It also flags a month whose total bill is more than 30% above the preceding month's bill.

## What it demonstrates

Variables, numbers, strings, tuples, lists, nested loops, conditions, arithmetic operators, comparison operators, and a repeated-character output pattern. No imports or user-defined functions are used.

## Sample assumptions

- First 100 units: 4.50 per unit.
- Next 100 units: 6.00 per unit.
- Remaining units: 8.00 per unit.
- Fixed charge: 75.
- Consumption above 250 units: 5% surcharge on energy charge.
- Consumption up to and including 100 units: 25 rebate.

Monthly usage and rate slabs are editable near the top of `main.py`.

## Algorithm

1. For each month, walk through the rate slabs and charge the consumed units.
2. Add the fixed fee and any surcharge, then subtract an applicable rebate.
3. Compare the bill with the previous month and print an alert if it exceeds 130%.
4. Save the current bill for the next comparison.

## Pseudocode

```text
FOR each month
    remaining = monthly units
    FOR each slab
        charge units remaining in that slab
    add fixed charge and applicable surcharge
    subtract applicable rebate
    IF bill > previous bill * 1.30, print alert
    previous bill = bill
```

## Flowchart

```text
START -> Read monthly usage -> Calculate slab charges -> Add fees/subtract rebate
       -> Compare with previous bill -> Print bill and alert if needed
       -> Next month? --yes--> Calculate next month
                    --no--> END
```

## Run

```powershell
python main.py
```

## Live Streamlit deployment

https://progressive-electricity-billing-eilqpz6ydcnusq8wkvagsp.streamlit.app/
