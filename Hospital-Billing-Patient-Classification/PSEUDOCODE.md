# Pseudocode: Hospital-Billing-Patient-Classification

```text
FOR each patient
    IF any input is invalid, report invalid record
    ELSE
        add charges and calculate concessions
        IF payment exceeds final bill, report invalid payment
        ELSE classify as fully paid, partial, or balance due
        print patient result
```
