# Manufacturing Cost and Profitability Analysis

Calculates sample production costs and evaluates whether each product meets its target profit rate.

## What it demonstrates

Variables, numbers, strings, tuples, lists, loops, conditions, arithmetic and comparison operators, and tuple unpacking. No imports or user-defined functions are used.

## Sample assumptions

- Material wastage is a percentage of total material cost.
- Labor cost is calculated per unit.
- Machine cost is a fixed batch cost.
- Profit rate is profit divided by total production cost.
- Profit equals sales revenue minus production cost.

Product data and target rates are editable at the top of `main.py`.

## Algorithm

1. Calculate material, wastage, labor, and machine costs for each batch.
2. Add the costs to find total production cost.
3. Calculate revenue, profit, and profit rate.
4. Compare the profit rate with the target and print the result.

## Pseudocode

```text
FOR each product batch
    calculate material cost and wastage
    calculate labor and machine costs
    total cost = sum of costs
    revenue = units * selling price
    profit rate = (revenue - total cost) / total cost
    compare with target and print analysis
```

## Flowchart

```text
START -> Read batch -> Calculate material, wastage, labor, machine costs
       -> Calculate total cost and revenue -> Calculate profit rate
       -> Target met? -> Print analysis -> Next batch or END
```

## Run

```powershell
python main.py
```

## Live Streamlit deployment

https://manufacturing-cost-profit-7er8wzs3bp7q3lnjqhnhuo.streamlit.app/
