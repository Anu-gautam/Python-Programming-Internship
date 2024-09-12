import tkinter as tk
from tkinter import simpledialog

class ToDoListGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.tasks = []

        # Create GUI widgets
        self.task_list_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.task_list_frame.pack(fill="both", expand=True)

        self.task_list = tk.Listbox(self.task_list_frame, width=40, font=("Helvetica", 12))
        self.task_list.pack(side="left", fill="both", expand=True)

        self.scrollbar = tk.Scrollbar(self.task_list_frame)
        self.scrollbar.pack(side="right", fill="y")
        self.task_list.config(yscrollcommand=self.scrollbar.set)
        self.scrollbar.config(command=self.task_list.yview)

        self.button_frame = tk.Frame(self.master, bg="#f0f0f0")
        self.button_frame.pack(fill="x")

        self.add_task_button = tk.Button(self.button_frame, text="Add Task", command=self.add_task, font=("Helvetica", 12), width=15)
        self.add_task_button.pack(side="left", padx=5, pady=5)

        self.delete_task_button = tk.Button(self.button_frame, text="Delete Task", command=self.delete_task, font=("Helvetica", 12), width=15)
        self.delete_task_button.pack(side="left", padx=5, pady=5)

    def add_task(self):
        task = simpledialog.askstring("Add Task", "Enter a task:")
        if task:
            self.tasks.append(task)
            self.task_list.insert(tk.END, task)

    def delete_task(self):
        task_number = simpledialog.askinteger("Delete Task", "Enter task number:")
        if task_number:
            del self.tasks[task_number - 1]
            self.task_list.delete(task_number - 1)

root = tk.Tk()
root.geometry("400x300")  # Set the window size
gui = ToDoListGUI(root)
root.mainloop()