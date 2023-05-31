import os
import tkinter as tk
from tkinter import ttk

def populate_treeview(parent, node):
    path = os.path.abspath(node)
    parent_node = treeview.insert(parent, 'end', text=node, open=False)

    for item in os.listdir(path):
        item_path = os.path.join(path, item)
        if os.path.isdir(item_path):
            populate_treeview(parent_node, item)

root = tk.Tk()
treeview = ttk.Treeview(root)
treeview.pack()

root_dir = os.getcwd()  # Replace with the desired directory path
populate_treeview('', root_dir)

root.mainloop()
