import argparse
import json
import os

# File to store tasks
TASKS_FILE = "tasks.json"

def load_tasks():
    """Load tasks from the JSON file."""
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    """Save tasks to the JSON file."""
    with open(TASKS_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(description):
    """Add a new task."""
    tasks = load_tasks()
    task = {"id": len(tasks) + 1, "description": description, "done": False}
    tasks.append(task)
    save_tasks(tasks)
    print(f"Task added: {description}")

def list_tasks():
    """List all tasks."""
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for task in tasks:
        status = "✓" if task["done"] else "✗"
        print(f"{task['id']}. [{status}] {task['description']}")

def update_task(task_id, new_description):
    """Update an existing task."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["description"] = new_description
            save_tasks(tasks)
            print(f"Task {task_id} updated.")
            return
    print(f"Task {task_id} not found.")

def delete_task(task_id):
    """Delete a task."""
    tasks = load_tasks()
    tasks = [task for task in tasks if task["id"] != task_id]
    save_tasks(tasks)
    print(f"Task {task_id} deleted.")

def mark_done(task_id):
    """Mark a task as done."""
    tasks = load_tasks()
    for task in tasks:
        if task["id"] == task_id:
            task["done"] = True
            save_tasks(tasks)
            print(f"Task {task_id} marked as done.")
            return
    print(f"Task {task_id} not found.")

# Set up argument parser
parser = argparse.ArgumentParser(description="Simple To-Do List CLI Tool")
subparsers = parser.add_subparsers(dest="command")

# Add task command
parser_add = subparsers.add_parser("add", help="Add a new task")
parser_add.add_argument("description", type=str, help="Task description")

# List tasks command
parser_list = subparsers.add_parser("list", help="List all tasks")

# Update task command
parser_update = subparsers.add_parser("update", help="Update a task")
parser_update.add_argument("id", type=int, help="Task ID")
parser_update.add_argument("description", type=str, help="New task description")

# Delete task command
parser_delete = subparsers.add_parser("delete", help="Delete a task")
parser_delete.add_argument("id", type=int, help="Task ID")

# Mark task as done command
parser_done = subparsers.add_parser("done", help="Mark a task as done")
parser_done.add_argument("id", type=int, help="Task ID")

# Parse arguments
args = parser.parse_args()

if args.command == "add":
    add_task(args.description)
elif args.command == "list":
    list_tasks()
elif args.command == "update":
    update_task(args.id, args.description)
elif args.command == "delete":
    delete_task(args.id)
elif args.command == "done":
    mark_done(args.id)
else:
    parser.print_help()
