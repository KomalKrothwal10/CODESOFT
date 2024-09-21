import tkinter as tk 
from tkinter import messagebox

class To_do_list:
    def __init__ (self,root):
        self.root = root
        self.root.title("To-Do-List")
        
        self.tasks = []
        self.task_frame = tk.Frame(self.root)
        self.task_frame.pack(pady=10)
        
        self.task_listbox = tk.Listbox(self.task_frame, width=50, height=10)
        self.task_listbox.pack(side=tk.LEFT)
        
        self.scrollbar = tk.Scrollbar(self.task_frame)
        self.scrollbar.pack(side = tk.RIGHT , fill = tk.Y)
        
        self.task_listbox.config(yscrollcommand = self.scrollbar.set)
        self.scrollbar.config(command=self.task_listbox.yview)

        self.entry_task = tk.Entry(self.root, width=52)
        self.entry_task.pack(pady=10)

        self.add_task_button = tk.Button(self.root, text="Add Task", command=self.add_task)
        self.add_task_button.pack(pady=5)

        self.remove_task_button = tk.Button(self.root, text="Remove Task", command=self.remove_task)
        self.remove_task_button.pack(pady=5)

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.tasks.append(task)
            self.update_task_list()
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def remove_task(self):
        try:
            selected_task_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_task_index)
            self.update_task_list()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to remove.")

    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = To_do_list(root)
    root.mainloop()
