# Day 012: File Handling - Reading

import os

def main():
    """Main function for Day 012: File Handling - Reading"""
    print("=" * 50)
    print("Day 012: File Handling - Reading")
    print("=" * 50)
    
    # Create a sample file for demonstration
    create_sample_file()
    
    # Different ways to read files
    read_entire_file()
    read_line_by_line()
    read_with_context_manager()
    read_specific_lines()

def create_sample_file():
    """Create a sample text file for demonstration"""
    content = """Python is awesome!
File handling is important.
Reading files is easy.
Practice makes perfect.
Keep coding every day!"""
    
    with open("sample.txt", "w") as f:
        f.write(content)
    print(" Sample file created\n")

def read_entire_file():
    """Read entire file at once"""
    print("=== Reading Entire File ===")
    with open("sample.txt", "r") as f:
        content = f.read()
        print(content)
    print()

def read_line_by_line():
    """Read file line by line"""
    print("=== Reading Line by Line ===")
    with open("sample.txt", "r") as f:
        for line_num, line in enumerate(f, 1):
            print(f"Line {line_num}: {line.strip()}")
    print()

def read_with_context_manager():
    """Using with statement (best practice)"""
    print("=== Using Context Manager ===")
    with open("sample.txt", "r") as f:
        lines = f.readlines()
        print(f"Total lines: {len(lines)}")
        print(f"First line: {lines[0].strip()}")
        print(f"Last line: {lines[-1].strip()}")
    print()

def read_specific_lines():
    """Read specific number of lines"""
    print("=== Reading Specific Lines ===")
    with open("sample.txt", "r") as f:
        first_line = f.readline()
        second_line = f.readline()
        print(f"First: {first_line.strip()}")
        print(f"Second: {second_line.strip()}")
    print()

if __name__ == "__main__":
    main()
    # Cleanup
    if os.path.exists("sample.txt"):
        os.remove("sample.txt")
        print(" Cleanup completed")
