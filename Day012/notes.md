# Day 012 Notes: File Handling - Reading

## Key Takeaways
- The `open()` function is the gateway to file handling.
- Always use context managers (`with` statement) to ensure files are closed properly.
- Different methods exist for reading: `read()` for all, `readline()` for one line, `readlines()` for a list.

## Important Concepts
- **Context Managers**: The `with open(...)` syntax automatically handles file closing, even if errors occur.
- **File Modes**: 'r' is for reading (default).
- **Cursors**: Reading moves the file cursor. You can't read the same content twice without seeking back.

## Code Snippets
```python
# Best practice: Use 'with'
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line (memory efficient)
with open('large_file.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

## Common Pitfalls
- Forgetting to close the file (solved by `with`).
- Assuming the file exists without error handling (`try-except FileNotFoundError`).
- Reading a huge file entirely into memory with `read()` instead of iterating.

## Practice Ideas
- Write a script to count words in a text file.
- Create a log reader that filters for "ERROR".
- Read a CSV file manually (before using the csv module).

