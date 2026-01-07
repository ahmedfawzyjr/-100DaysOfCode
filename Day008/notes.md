# Day 008 Notes

## Key Takeaways
- Use get() method to avoid KeyError
- Keys must be immutable (strings, numbers, tuples)
- Values can be any type
- Dictionary comprehensions: {k: v for ...}

## Common Dictionary Methods
- get(key, default) - Safe access
- keys() - Get all keys
- values() - Get all values
- items() - Get key-value pairs
- pop(key) - Remove and return value
- update(dict) - Merge dictionaries
- clear() - Remove all items

## Dictionary Patterns
```python
# Default value
count = d.get(key, 0)

# Check and add
if key not in d:
    d[key] = value

# Iterate items
for k, v in d.items():
    print(k, v)
```

## Practice Ideas
- Build a phonebook app
- Create an inventory system
- Make a quiz game with scores
