# Day 007 Notes

## Key Takeaways
- Tuples are immutable - cannot add, remove, or change elements
- Use tuples for data that shouldn't change
- Tuples are faster and use less memory than lists
- Single element tuple needs trailing comma: (x,)

## Tuples vs Lists
| Feature | Tuple | List |
|---------|-------|------|
| Mutability | Immutable | Mutable |
| Syntax | () | [] |
| Performance | Faster | Slower |
| Use Case | Fixed data | Dynamic data |

## When to Use Tuples
- Returning multiple values from functions
- Dictionary keys (lists can't be keys)
- Data that shouldn't change (coordinates, RGB values)

## Practice Ideas
- Create a contact book with tuples
- Build a coordinate geometry calculator
- Make a color palette manager
