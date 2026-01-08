# Day 009 Notes

## Key Takeaways
- Sets automatically remove duplicates
- Unordered - no indexing
- Fast membership testing O(1)
- Use for mathematical set operations

## Set Operations
| Operation | Operator | Method |
|-----------|----------|--------|
| Union | \| | union() |
| Intersection | & | intersection() |
| Difference | - | difference() |
| Symmetric Diff | ^ | symmetric_difference() |

## Set Methods
- add(x) - Add element
- remove(x) - Remove (raises error if not found)
- discard(x) - Remove (no error)
- pop() - Remove and return arbitrary element
- clear() - Remove all elements
- copy() - Shallow copy

## When to Use Sets
- Remove duplicates from a list
- Fast membership testing
- Mathematical set operations
- Finding unique elements

## Practice Ideas
- Build a tag manager
- Create a unique visitor counter
- Make a Venn diagram calculator
