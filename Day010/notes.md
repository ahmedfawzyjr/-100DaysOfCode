# Day 010 Notes

## Key Takeaways
- Functions are defined with `def` keyword
- Use descriptive function names (verb_noun pattern)
- Always include docstrings for documentation
- Return None if no explicit return statement
- Functions can return multiple values as tuple

## Function Structure
```python
def function_name(parameters):
    """Docstring describing function"""
    # Function body
    return value
```

## Best Practices
- One function, one purpose (Single Responsibility)
- Use meaningful parameter names
- Keep functions short and focused
- Document with docstrings
- Return early for edge cases

## Common Patterns
```python
# Guard clause
def divide(a, b):
    if b == 0:
        return None
    return a / b

# Multiple returns
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)
```

## Practice Ideas
- Create a math utilities library
- Build string manipulation functions
- Make a validation function collection
