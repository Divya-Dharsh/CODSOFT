import tkinter as tk
from tkinter import PhotoImage, messagebox

# Initialize the main window
root = tk.Tk()
root.title("TO DO LIST")
root.geometry("400x400")
root.configure(bg="#F3E8FF")

# Background image
bg_image = PhotoImage(file="background.png") # Ensure you have a background.png image in the same directory
background_label = tk.Label(root, image=bg_image)
background_label.place(relwidth=1, relheight=1)

tasks = []  # Tasks will be stored as strings

# Function to update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Function to add a new task 
def add_task():
    task = task_entry.get()
    if task.strip():  # Check for non-empty task
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# Function to delete a selected task 
def delete_task():
    try:
        task_index = listbox.curselection()[0]
        tasks.pop(task_index)
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# Function to mark a task as completed
def mark_task_completed():
    try:
        task_index = listbox.curselection()[0]
        tasks[task_index] += " [Completed]"
        update_listbox()
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

# Function to edit a selected task
def edit_task():
    try:
        task_index = listbox.curselection()[0]
        new_task = task_entry.get()
        if new_task.strip():
            tasks[task_index] = new_task
            update_listbox()
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a new task name.")
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# UI Elements
title_label = tk.Label(root, text="My To-Do List", font=("Helvetica", 24, "bold"), bg="#D291BC", fg="#FFF")
title_label.pack(pady=10)

task_entry = tk.Entry(root, width=40, font=("Helvetica", 14), borderwidth=3, relief="solid")
task_entry.pack(pady=10)

button_frame = tk.Frame(root, bg="#F3E8FF")
button_frame.pack(pady=10)

add_button = tk.Button(button_frame, text="Add Task", width=12, font=("Helvetica", 12), bg="#82C4F4", fg="white", command=add_task)
add_button.grid(row=0, column=0, padx=5)

delete_button = tk.Button(button_frame, text="Delete Task", width=12, font=("Helvetica", 12), bg="#FF6F61", fg="white", command=delete_task)
delete_button.grid(row=0, column=1, padx=5)

edit_button = tk.Button(button_frame, text="Edit Task", width=12, font=("Helvetica", 12), bg="#FFD700", fg="black", command=edit_task)
edit_button.grid(row=1, column=0, padx=5, pady=5)

complete_button = tk.Button(button_frame, text="Mark as Completed", width=16, font=("Helvetica", 12), bg="#8BC34A", fg="white", command=mark_task_completed)
complete_button.grid(row=1, column=1, padx=5, pady=5)

listbox_frame = tk.Frame(root, bg="#F3E8FF")
listbox_frame.pack(pady=20)

listbox = tk.Listbox(listbox_frame, height=10, width=45, font=("Helvetica", 14), bg="#FFFDD0", fg="#333", selectbackground="#FFB6C1", selectforeground="#000")
listbox.pack(side="left", fill="y")

scrollbar = tk.Scrollbar(listbox_frame, orient="vertical")
scrollbar.config(command=listbox.yview)
scrollbar.pack(side="right", fill="y")

listbox.config(yscrollcommand=scrollbar.set)

# Run the main loop
root.mainloop()
