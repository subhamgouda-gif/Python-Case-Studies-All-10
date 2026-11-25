# Employee Payroll and Deduction Analysis

Produces a sample payroll statement with overtime, allowances, incentives, provident-fund deductions, professional tax, and progressive income tax.

## What it demonstrates

Variables, arithmetic, numbers, strings, tuples, a list of employee records, loops, conditions, and tuple unpacking. No imports or user-defined functions are used.

## Sample assumptions

- Tax is 5% on the first 30000, 10% on the next 40000, and 15% above 70000.
- Provident-fund deduction is 8% of basic salary.
- Professional tax is 200 per employee.
- Gross pay includes basic salary, housing and transport allowances, overtime, and incentive.

Change the employee records or assumptions at the top of `main.py`.

## Algorithm

1. Calculate overtime pay and gross pay for each employee.
2. Apply the tax rates progressively to the corresponding salary bands.
3. Calculate provident fund and professional tax.
4. Subtract all deductions from gross pay and display the statement.

## Pseudocode

```text
FOR each employee
    overtime pay = hours * overtime rate
    gross pay = salary + allowances + overtime + incentive
    calculate tax in each progressive band
    deductions = tax + provident fund + professional tax
    net pay = gross pay - deductions
    print payroll statement
```

## Flowchart

```text
START -> Read employee -> Calculate gross pay -> Calculate progressive tax
       -> Calculate other deductions -> Calculate net pay -> Print statement
       -> Next employee? --yes--> Repeat
                        --no--> END
```

## Run

```powershell
python main.py
```

## Live Streamlit deployment

https://employee-payroll-analysis-sdtw4czfwjcksrtzypxbk5.streamlit.app/
