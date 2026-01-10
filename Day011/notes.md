# Day 011 Notes

## Key Takeaways
- Default parameters must come after non-default ones
- *args captures extra positional arguments as tuple
- **kwargs captures extra keyword arguments as dict
- Lambda syntax: lambda parameters: expression
- Closures remember enclosing scope variables

## Function Signature Order
```python
def func(pos_arg, default_arg=value, *args, **kwargs):
    pass
```

## Lambda vs Regular Function
```python
# Regular
def square(x):
    return x ** 2

# Lambda
square = lambda x: x ** 2
```

## When to Use Lambda
- Simple one-line operations
- As arguments to map(), filter(), sorted()
- Callback functions
- NOT for complex logic

## Scope (LEGB Rule)
1. **L**ocal - Inside function
2. **E**nclosing - In enclosing function
3. **G**lobal - Module level
4. **B**uilt-in - Python built-ins

## Practice Ideas
- Build a flexible logging function
- Create a decorator function
- Make a function factory
