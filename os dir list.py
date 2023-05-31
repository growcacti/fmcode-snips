import os
import tkinter as tk

def populate_listbox():
    path = os.getcwd()  # Replace with the desired directory path
    directories = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    listbox.delete(0, tk.END)  # Clear the listbox
    for directory in directories:
        listbox.insert(tk.END, directory)

def on_listbox_select(event):
    selected_index = listbox.curselection()
    if selected_index:
        selected_item = listbox.get(selected_index)
        selected_path = os.path.join(path, selected_item)
        print(selected_path)  # Do something with the selected path

root = tk.Tk()
listbox = tk.Listbox(root)
listbox.pack()

populate_listbox()
listbox.bind("<<ListboxSelect>>", on_listbox_select)

root.mainloop()
