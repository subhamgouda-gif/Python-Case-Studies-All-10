# Pseudocode: Progressive-Electricity-Billing

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
