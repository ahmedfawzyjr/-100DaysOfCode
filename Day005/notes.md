# Day 005 Notes

## Key Takeaways
- While loops are condition-based
- Always update the condition variable inside the loop
- Use break to exit early
- Use continue to skip iterations
- while-else: else block runs if loop completes normally

## Avoiding Infinite Loops
```python
# BAD - Infinite loop
while True:
    print("Forever")

# GOOD - Has exit condition
count = 0
while count < 10:
    print(count)
    count += 1
```

## Practice Ideas
- Create a menu-driven program
- Build a simple ATM simulator
- Make a password generator with validation
