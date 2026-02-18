# Day 050: CRUD Operations

import sqlite3
import os

class TaskManager:
    """Simple task manager demonstrating CRUD operations"""
    
    def __init__(self, db_name="tasks.db"):
        self.db_name = db_name
        self.create_table()
    
    def create_table(self):
        """CREATE: Create tasks table"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT,
                status TEXT DEFAULT 'pending',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        conn.commit()
        conn.close()
    
    def create_task(self, title, description=""):
        """CREATE: Add a new task"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            "INSERT INTO tasks (title, description) VALUES (?, ?)",
            (title, description)
        )
        conn.commit()
        task_id = cursor.lastrowid
        conn.close()
        print(f" Task created with ID: {task_id}")
        return task_id
    
    def read_all_tasks(self):
        """READ: Get all tasks"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks")
        tasks = cursor.fetchall()
        conn.close()
        return tasks
    
    def read_task(self, task_id):
        """READ: Get a specific task"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tasks WHERE id = ?", (task_id,))
        task = cursor.fetchone()
        conn.close()
        return task
    
    def update_task(self, task_id, title=None, description=None, status=None):
        """UPDATE: Modify a task"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        
        if title:
            cursor.execute("UPDATE tasks SET title = ? WHERE id = ?", (title, task_id))
        if description:
            cursor.execute("UPDATE tasks SET description = ? WHERE id = ?", (description, task_id))
        if status:
            cursor.execute("UPDATE tasks SET status = ? WHERE id = ?", (status, task_id))
        
        conn.commit()
        conn.close()
        print(f" Task {task_id} updated")
    
    def delete_task(self, task_id):
        """DELETE: Remove a task"""
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        conn.commit()
        conn.close()
        print(f" Task {task_id} deleted")
    
    def display_tasks(self):
        """Display all tasks"""
        tasks = self.read_all_tasks()
        if not tasks:
            print("No tasks found.")
            return
        
        print("\n" + "=" * 70)
        print(f"{'ID':<5} {'Title':<20} {'Status':<10} {'Description':<30}")
        print("=" * 70)
        for task in tasks:
            task_id, title, desc, status, _ = task
            print(f"{task_id:<5} {title:<20} {status:<10} {desc:<30}")
        print("=" * 70 + "\n")

def main():
    """Demonstrate CRUD operations"""
    print("=" * 50)
    print("Day 050: CRUD Operations")
    print("=" * 50)
    
    # Initialize task manager
    tm = TaskManager()
    
    # CREATE
    print("\n=== CREATE Operations ===")
    tm.create_task("Learn Python", "Complete 100 days of code")
    tm.create_task("Build Project", "Create a web application")
    tm.create_task("Read Documentation", "Study Flask docs")
    
    # READ
    print("\n=== READ Operations ===")
    tm.display_tasks()
    
    # UPDATE
    print("=== UPDATE Operations ===")
    tm.update_task(1, status="completed")
    tm.update_task(2, description="Create a Flask web app")
    tm.display_tasks()
    
    # DELETE
    print("=== DELETE Operations ===")
    tm.delete_task(3)
    tm.display_tasks()
    
    # Cleanup
    if os.path.exists("tasks.db"):
        os.remove("tasks.db")
        print(" Database cleaned up")

if __name__ == "__main__":
    main()
