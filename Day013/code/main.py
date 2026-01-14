def main():
    """
    Main function for Day 13: File Handling - Writing
    """
    print("=" * 50)
    print(f"Day 13: File Handling - Writing")
    print("=" * 50)
    
    # Example code
    example_file_writing()

def example_file_writing():
    """Example implementation for File Handling - Writing"""
    filename = "day13_demo.txt"
    
    # 1. Writing to a file (w mode) - Creates or overwrites
    print(f"\n[1] Writing to '{filename}' with 'w' mode...")
    with open(filename, 'w') as f:
        f.write("Hello, World!\n")
        f.write("This file was created using Python.\n")
    print("File created and written successfully.")
    
    # Verify content
    print("Content after 'w' mode:")
    read_file(filename)
    
    # 2. Overwriting the file (w mode again)
    print(f"\n[2] Overwriting '{filename}' with 'w' mode...")
    with open(filename, 'w') as f:
        f.write("This is new content.\n")
        f.write("The old content is gone.\n")
    print("File overwritten successfully.")
    
    # Verify content
    print("Content after overwrite:")
    read_file(filename)
    
    # 3. Appending to a file (a mode)
    print(f"\n[3] Appending to '{filename}' with 'a' mode...")
    with open(filename, 'a') as f:
        f.write("This line is appended.\n")
        f.write("Data persistence is awesome!\n")
    print("Data appended successfully.")
    
    # Verify content
    print("Content after 'a' mode:")
    read_file(filename)

def read_file(filename):
    """Helper to read and print file content"""
    try:
        with open(filename, 'r') as f:
            print("-" * 20)
            print(f.read().strip())
            print("-" * 20)
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

if __name__ == "__main__":
    main()
