# Pseudocode: Railway-Fare-Reservation

```text
FOR each passenger
    find class rate
    IF passenger or class is invalid, report invalid record
    ELSE calculate fare by distance slabs
        apply age concession and add reservation fee
        IF cancelled, calculate cancellation fee and refund
        ELSE print reservation fare
```
