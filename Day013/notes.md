# Day 013 Notes: File Handling - Writing
 
 ## Key Takeaways
 - `w` mode: Opens a file for writing. Creates a new file if it doesn't exist or truncates (overwrites) the file if it does.
 - `a` mode: Opens a file for appending. Creates a new file if it doesn't exist. The file pointer is at the end of the file if the file exists.
 - Always close files or use the `with` statement to ensure resources are released.
 
 ## Important Concepts
 - **Writing (`w`)**: Destructive operation for existing files. Good for creating new files or completely refreshing content.
 - **Appending (`a`)**: Non-destructive. Adds data to the end. Useful for logs or accumulating data.
 - **Newline (`\n`)**: `write()` does not add a newline automatically; you must include `\n` explicitly.
 
 ## Code Snippets
 ```python
 # Writing (Overwrites existing content)
 with open("file.txt", "w") as f:
     f.write("Hello, World!\n")
 
 # Appending (Adds to the end)
 with open("file.txt", "a") as f:
     f.write("Appending new line.\n")
 ```
 
 ## Common Pitfalls
 - Forgetting `\n` creates one long line of text.
 - Using `w` instead of `a` accidentally wipes out important data.
 - Not closing the file (though `with` handles this).
 
 ## Practice Ideas
 - Create a simple logger that appends timestamps and messages to a file.
 - Write a program that takes user input and saves it to a file.
