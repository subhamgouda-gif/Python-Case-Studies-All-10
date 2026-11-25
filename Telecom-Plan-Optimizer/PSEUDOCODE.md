# Pseudocode: Telecom-Plan-Optimizer

```text
FOR each subscriber
    best plan = none
    FOR each plan
        calculate excess data and total price
        IF validity and budget pass
            keep plan if cheaper, or longer if tied
    print best plan or no-match message
```
