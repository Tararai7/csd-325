# Name: Tara Rai
# Course :M10.2
# Date: 02/8/2026

import tkinter as tk
from tkinter import messagebox

class ToDoApp:
    def __init__(self, root):
        self.root = root
        # Requirement 1: Change Title to Last Name-ToDo
        self.root.title("Rai-ToDo") 
        self.root.geometry("500x400")
        
        # Requirement 2: Change color of menu items (Complementary Colors)
        # Using Dark Blue (#1E3A8A) and Orange (#F97316)
        self.menu_bar = tk.Menu(root, bg="#1E3A8A", fg="#F97316")
        root.config(menu=self.menu_bar)
        
        # Requirement 5: Add Menu Item File -> Exit
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0, bg="#1E3A8A", fg="#F97316")
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Exit", command=self.exit_app)
        
        # Requirement 4: Provide instructions in the label on how to delete
        self.instruction_label = tk.Label(
            root, 
            text="Added --- ** Right Click Item to Delete**",
            bg="#F97316",
            fg="#1E3A8A",
            font=("Arial", 10, "bold")
        )
        self.instruction_label.pack(fill=tk.X, padx=5, pady=5)
        
        # Create frame for listbox and scrollbar
        self.frame = tk.Frame(root)
        self.frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Create scrollbar
        self.scrollbar = tk.Scrollbar(self.frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        
        # Create listbox with complementary colors
        self.todo_list = tk.Listbox(
            self.frame,
            bg="#1E3A8A",  # Dark blue background
            fg="#F97316",  # Orange foreground
            font=("Arial", 12),
            selectbackground="#F97316",
            selectforeground="#1E3A8A",
            yscrollcommand=self.scrollbar.set
        )
        self.todo_list.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        # Configure scrollbar
        self.scrollbar.config(command=self.todo_list.yview)
        
        # Requirement 3: Change delete to right mouse button (Button-3)
        self.todo_list.bind("<Button-3>", self.delete_task)
        
        # Entry field for new tasks
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(fill=tk.X, padx=10, pady=5)
        self.entry.bind("<Return>", self.add_task)
        
        # Add button
        self.add_button = tk.Button(
            root, 
            text="Add Task", 
            command=self.add_task,
            bg="#F97316",
            fg="#1E3A8A",
            font=("Arial", 10, "bold")
        )
        self.add_button.pack(pady=5)
    
    def add_task(self, event=None):
        task = self.entry.get()
        if task:
            self.todo_list.insert(tk.END, task)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task!")
    
    def delete_task(self, event):
        # Get the index of the item clicked with right mouse button
        index = self.todo_list.nearest(event.y)
        self.todo_list.delete(index)
    
    def exit_app(self):
        # Confirm exit
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoApp(root)
    root.mainloop()