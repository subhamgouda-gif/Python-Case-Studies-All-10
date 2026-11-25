# Multi-Currency Travel Budget Analysis

Converts sample travel expenses to INR, adds a conversion fee, finds the largest expense category, and compares spending with a budget.

## What it demonstrates

Variables, numbers, strings, tuples, lists, nested loops, conditions, arithmetic and comparison operators, indexing, and list operations. No imports or user-defined functions are used.

## Sample assumptions

- Each expense has a sample exchange rate expressed as INR per unit of foreign currency.
- A 2% conversion fee is added to the converted INR amount.
- Expenses with the same category are combined when finding the largest category.
- The budget is 120000 INR.

Exchange rates, expenses, fee, and budget are editable near the top of `main.py`. Rates are examples, not live financial data.

## Algorithm

1. Convert every expense to INR and calculate its conversion fee.
2. Add the result to total spending.
3. Search the category list; add to its total or create a new category total.
4. Find the category with the greatest total.
5. Compare total spending with the budget and print the remaining amount or overspend.

## Pseudocode

```text
FOR each expense
    convert amount and calculate fee
    add converted total to overall spending
    find category and add to category total
find category with greatest total
compare overall spending with budget
print results
```

## Flowchart

```text
START -> Read expenses and rates -> Convert each amount and add fee
       -> Update category and overall totals -> More expenses? --yes--> Repeat
                                                  | no
                                                  v
                            Find largest category -> Compare budget -> END
```

## Run

```powershell
python main.py
```

## Live Streamlit deployment

https://multi-currency-travel-budget-leyjxra3n2zftcvwycdlhf.streamlit.app/

## Execution evidence

- [Pseudocode](PSEUDOCODE.md)
- [Terminal run screenshot](terminal-output.png)
