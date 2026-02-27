import tkinter as tk
from tkinter import Menu

def open_file():
    print("File > Open command clicked")

def save_file():
    print("File > Save command clicked")

def cut_text():
    print("Edit > Cut command clicked")

def copy_text():
    print("Edit > Copy command clicked")

def paste_text():
    print("Edit > Paste command clicked")

def about():
    print("Help > About command clicked")

root = tk.Tk()
root.title("Menu Example")

menu_bar = Menu(root)
root.config(menu=menu_bar)

# File menu
file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=root.destroy)

# Edit menu
edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut_text)
edit_menu.add_command(label="Copy", command=copy_text)
edit_menu.add_command(label="Paste", command=paste_text)

# Help menu
help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=about)

root.mainloop()