# Campus Event Financial Planning

Estimates an event budget, calculates the funding shortfall and per-attendee contribution, and finds the minimum registration count needed to break even.

## What it demonstrates

Variables, numbers, strings, arithmetic and comparison operators, conditions, a `while` loop, and repeated-character output patterns. No imports or user-defined functions are used.

## Sample assumptions

- Venue and equipment costs are fixed.
- Catering, transport, and certificates are charged per attendee.
- Sponsorship is a fixed contribution.
- Every registration pays the same fee.
- Break-even is the first registration count where sponsorship plus registration income is at least fixed plus variable costs.
- The search is limited to 10000 registrations; the program reports if the target is not reached.

Change the attendee count, costs, sponsorship, or fee at the top of `main.py`.

## Algorithm

1. Add fixed costs and calculate variable costs for planned attendance.
2. Calculate registration income, total income, shortfall, and the shortfall per planned attendee.
3. Compare registration fee per person with variable cost per person.
4. If break-even is possible, increase a candidate registration count until income covers costs.
5. Print the minimum count and projected totals.

## Pseudocode

```text
calculate planned total cost and income
shortfall = total cost - total income, but not below zero
IF registration fee cannot cover variable cost
    report whether break-even is possible
ELSE
    registrations = 0
    WHILE projected income < projected cost
        increase registrations by one
    print registrations and projected totals
```

## Flowchart

```text
START -> Read event assumptions -> Calculate planned costs and income
       -> Calculate shortfall -> Registration margin positive?
           | no -> Report break-even limitation
           | yes -> Increase registrations until income >= cost
       -> Print financial plan -> END
```

## Run

```powershell
python main.py
```

## Live Streamlit deployment

https://campus-event-financial-planning-jlddqsntydp94rxtkbcvhy.streamlit.app/
