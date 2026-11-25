# Hospital Billing and Patient Classification

Calculates sample patient bills, applies age and income concessions, validates payments, and classifies payment status.

## What it demonstrates

Variables, numbers, strings, tuples, a list of patient records, loops, conditions, arithmetic and comparison operators, and tuple unpacking. The script has no imports or user-defined functions.

## Sample assumptions

- A patient aged 60 or older receives 10% off.
- Income up to 200000 receives an additional 5% off.
- Combined concessions are capped at 15%.
- Payment equal to the bill means fully paid; at least 50% means partial payment; otherwise a balance is due.
- Negative charges, age, income, or payment are invalid. Payment above the final bill is also invalid.

The patient examples and assumptions are editable in `main.py`.

## Algorithm

1. Check patient charges, age, income, and payment for invalid values.
2. Add consultation, diagnostics, and treatment charges.
3. Calculate eligible concessions and subtract them from the gross bill.
4. Validate the amount paid and compare it with the final bill.
5. Print the bill, balance, and payment classification.

## Pseudocode

```text
FOR each patient
    IF any input is invalid, report invalid record
    ELSE
        add charges and calculate concessions
        IF payment exceeds final bill, report invalid payment
        ELSE classify as fully paid, partial, or balance due
        print patient result
```

## Flowchart

```text
START -> Read patient -> Valid amounts? --no--> Print invalid record
                              | yes
                              v
                    Calculate bill and concession
                              |
                    Payment within bill? --no--> Print invalid payment
                              | yes
                              v
                    Classify payment -> Print -> Next patient or END
```

## Run

```powershell
python main.py
```

## Live Streamlit deployment

https://hospital-billing-patient-classification-7ghuwuf6qys5d9pqwy4qgy.streamlit.app/

## Execution evidence

- [Pseudocode](PSEUDOCODE.md)
- [Terminal run screenshot](terminal-output.png)
