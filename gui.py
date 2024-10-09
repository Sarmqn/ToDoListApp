# GUI for the To-Do List Applicaiton

# gui.py
import tkinter as tk
from tkinter import messagebox, simpledialog
from ToDoList import save_tasks, load_tasks, add_task, mark_completed, delete_task

# Initialise the application window
root = tk.Tk()
root.title("To-Do List App")
# Application Window Size
root.geometry("1024x768")
# Default Light Mode
root.config(bg="#f0f0f0")

# Global tasks list loads tasks when application starts
tasks = load_tasks()

# Tracks current theme in a variable
is_dark_mode = False

# Function that updates the displayed task list
def update_task_list():
    task_list.delete(0, tk.END)
    sorted_tasks = get_sorted_tasks(tasks)
    for task in sorted_tasks:
        status = "✓" if task["Completed"] else "X"
        priority_map = {'1': 'High', '2': 'Medium', '3': 'Low'}
        priority_text = priority_map.get(task['priority'], 'N/A')
        task_list.insert(tk.END, f"{task['task']} [{status}] - Priority: {priority_text}")
        
# Function that helps to switch between different background colour modes
def toggle_mode():
    global is_dark_mode
    if is_dark_mode:
        # Switch to light mode
        root.config(bg = "#f0f0f0")
        task_list.config(bg ='#ffffff', fg = "#000000")
        for button in [add_task_button, mark_completed_button, delete_task_button]:
            button.config(bg = "#4CAF50", fg = "white")
        task_entry.config(bg = "#ffffff", fg = "#000000")
        is_dark_mode = False
        mode_button.config(text = "Switch to Dark Mode")
    else:
        # Switch to dark mode
        root.config(bg = "#2c2c2c")
        task_list.config(bg="#444444", fg = "#ffffff")
        for button in [add_task_button, mark_completed_button, delete_task_button]:
            button.config(bg = "#555555", fg = "white")
        task_entry.config(bg = "#555555", fg = "#ffffff")
        is_dark_mode = True
        mode_button.config(text = "Switch to Light Mode")
 
# Function to add tasks onto the gui
def add_task_gui():
    task = task_entry.get()
    if task:
        priority = simpledialog.askstring(" Task Priority", "Enter task priority (1 for High, 2 for Medium, 3 for Low):")
        if priority in ['1', '2', '3']:
            add_task(tasks, task, priority)
            update_task_list()
            task_entry_list()
        else:
            messagebox.showerror("Invalid Input", "Please enter 1, 2, or 3 for priority.")
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")
        
# Function to mark tasks as completed on the gui
def mark_completed_gui():
    try:
        selected_task_index = task_list.curselection()[0]
        mark_completed(tasks, selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to mark as completed.")
       
# Function to delete a task onto the gui
def delete_task_gui():
    try:
        selected_task_index = task_list.curselection()[0]
        delete_task(tasks, selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Select Task", "Please select a task to delete.")
        
# Creating frames to improve layout organisation
frame = tk.Frame(root, bg = "#f0f0f0")
frame.pack(pady=10)

task_label = tk.Label(frame, text = "Task:", bg = "#f0f0f0", font = ("Helvetica", 14))
task_label.pack(side = tk.LEFT)

task_entry = tk.Entry(frame, width = 30, font = ("Helvetica", 14))
task_entry.pack(side = tk.LEFT)

add_task_button = tk.Button(frame, text = "Add Task", command = add_task_gui, bg = "#4CAF50", fg = "white", font = ("Helvetica", 14))
add_task_button.pack(side = tk.LEFT)

# Creating a listbox to display the tasks
task_list = tk.Listbox(root, width = 50, height = 15, font = ("Helvetica", 14), bg = "#ffffff", selectbackground="#D1E7DD")
task_list.pack(pady=20)

# Creating buttons for actions
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=10)

mark_completed_button = tk.Button(button_frame, text="Mark Completed", command=mark_completed_gui, bg="#2196F3", fg="white", font=("Helvetica", 14))
mark_completed_button.pack(side=tk.LEFT, padx=5)

delete_task_button = tk.Button(button_frame, text="Delete Task", command=delete_task_gui, bg="#F44336", fg="white", font=("Helvetica", 14))
delete_task_button.pack(side=tk.LEFT, padx=5)

# Update the task list on startup
update_task_list()

# Start the main loop
root.mainloop()