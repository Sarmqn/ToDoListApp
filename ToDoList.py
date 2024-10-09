import json

# Function that makes tasks save in a text file
def save_tasks(tasks):
    with open('tasks.txt', 'w') as file:
        json.dump(tasks, file)
    print("Tasks have been saved to 'tasks.txt'.")

# Function to load tasks from a file
def load_tasks():
    try:
        with open('tasks.txt', 'r') as file:
            tasks = json.load(file)
        print("Tasks loaded from 'tasks.txt'.")
        return tasks
    except FileNotFoundError:
        print("No saved tasks have been found.")
        return []

# Function that adds tasks to the task list
def add_task(tasks, task, priority):
    task = input("Enter a new task: ")
    
    # Initialize the priority variable
    priority = None  
    # Check for valid priority
    while priority not in ['1', '2', '3']:
        priority = input("Enter task priority (1 for High, 2 for Medium, 3 for Low): ")
        
        # Validate priority input
        if priority not in ['1', '2', '3']:
            print("Invalid priority! Please enter 1, 2, or 3.")
    
    tasks.append({"task": task, "completed": False, "priority": int(priority)})
    print(f"'{task}' has been added to your To-Do List with priority {priority}.")

# Function that allows viewing of tasks with integrated sorting
def view_tasks(tasks):
    if not tasks:
        print("Your To-Do List is empty!")
    else:
        # Sort tasks by priority before displaying
        priority_order = {'1': 1, '2': 2, '3': 3}
        sorted_tasks = sorted(tasks, key=lambda x: priority_order.get(x['priority'], 4))
        
        print("\nYour To-Do List:")
        for i, task in enumerate(sorted_tasks, 1):  # No need for get_sorted_tasks
            status = "✓" if task['completed'] else "✗"
            priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
            priority_text = priority_map.get(task['priority'], 'N/A')
            print(f"{i}. {task['task']} [{status}] - Priority: {priority_text}")

# Function that marks tasks as completed
def mark_completed(tasks):
    if not tasks:
        print("Your To-Do List is empty!")
    else:
        view_tasks(tasks)
        task_num = int(input("Enter the task number to mark as completed: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]['completed'] = True
            print(f"Task {task_num} marked as completed.")
        else:
            print("Invalid task number.")

# Function that enables the removal of tasks
def delete_task(tasks):
    if not tasks:
        print("Your To-Do List is empty!")
    else:
        view_tasks(tasks)
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Deleted task: {removed_task['task']}")
        else:
            print("Invalid task number!")

# Menu with options
def show_menu():
    print("\n To-Do List Menu:")
    print("1. Add a task")
    print("2. View Tasks")
    print("3. Mark a task as completed")
    print("4. Delete a task")
    print("5. Save tasks")
    print("6. Load tasks")
    print("7. Exit")

# To-Do List Application
def main():
    tasks = [] 
    
    while True:
        show_menu()
        choice = input("Choose an option please: ")
        
        if choice == '1':
            add_task(tasks)
        elif choice == '2':
            view_tasks(tasks)
        elif choice == '3':
            mark_completed(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
        elif choice == '6':
            tasks = load_tasks()
        elif choice == '7':
            print("Exiting, Goodbye!")
            break
        else:
            print("Invalid Choice. Please Select Again.")

if __name__ == "__main__":
    main()
