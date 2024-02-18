

import tkinter as tk
from tkinter import ttk
import tkinter.messagebox as messagebox
import os

class FileRenamerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Renamer Tool")
        self.root.geometry("800x600")  # Adjust size as needed
        self.file_type_vars = {}
        self.create_widgets()



    def create_widgets(self):
        # Create a label for the TreeView frame
        self.tree_label = tk.Label(self.root, text="Directory Structure")
        self.tree_label.grid(row=0, column=0, padx=10, pady=(10,0), sticky="nw")

        # Frame for the TreeView
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.grid(row=1, column=0, padx=10, pady=(0,10), sticky="nsew")

        # Continue with your TreeView setup...

        # Frame for the File Lists and File Type Filters
        self.list_frame = tk.Frame(self.root)
        self.list_frame.grid(row=0, column=1, rowspan=2, padx=10, pady=10, sticky="nsew")

        # Labels for the ListBoxes
        self.original_file_list_label = tk.Label(self.list_frame, text="Original File Names")
        self.original_file_list_label.grid(row=0, column=0, padx=5, pady=(0,5), sticky="nw")

        self.changed_file_list_label = tk.Label(self.list_frame, text="Changed File Names")
        self.changed_file_list_label.grid(row=0, column=1, padx=5, pady=(0,5), sticky="nw")

        # Listbox for original file names
        self.original_file_list = tk.Listbox(self.list_frame, height=20, width=50)
        self.original_file_list.grid(row=1, column=0, padx=5, pady=5)

        # Listbox for changed file names
        self.changed_file_list = tk.Listbox(self.list_frame, height=20, width=50)
        self.changed_file_list.grid(row=1, column=1, padx=5, pady=5)

  
        # Frame for the TreeView
        self.tree_frame = tk.Frame(self.root)
        self.tree_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # TreeView for directory structure
        self.tree = ttk.Treeview(self.tree_frame, columns=("Directory Structure",), show="tree")
        self.tree.pack(side="left", fill="both", expand=True)

        # Scrollbar for the TreeView
        self.tree_scroll = tk.Scrollbar(self.tree_frame, orient="vertical", command=self.tree.yview)
        self.tree.set_yscrollcommand=self.tree_scroll.set
        self.tree_scroll.pack(side="right", fill="y")

        # Frame for the File Lists and File Type Filters
        self.list_frame = tk.Frame(self.root)
        self.list_frame.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Listbox for original file names
        self.original_file_list = tk.Listbox(self.list_frame, height=20, width=50)
        self.original_file_list.grid(row=0, column=0, padx=5, pady=5)

        # Listbox for changed file names
        self.changed_file_list = tk.Listbox(self.list_frame, height=20, width=50)
        self.changed_file_list.grid(row=0, column=1, padx=5, pady=5)

        # Entry and Button for adding file types
        self.add_file_type_entry = tk.Entry(self.list_frame)
        self.add_file_type_entry.grid(row=1, column=0, padx=5, pady=5, sticky="ew")
        self.add_file_btn = tk.Button(self.list_frame, text="Add File Type", command=self.add_file_type)
        self.add_file_btn.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

        self.btn1 = tk.Button(self.list_frame, text="pop trereview", command=self.populate_treeview)
        self.btn1.grid(row=2, column=1, padx=5, pady=5, sticky="ew")
        self.tree.bind('<<TreeviewSelect>>', self.update_file_lists)
        # Configure the grid to be responsive
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.list_frame.grid_rowconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(0, weight=1)
        self.list_frame.grid_columnconfigure(1, weight=1)
        # In create_widgets method, after initializing other components
        self.rename_rule_frame = tk.Frame(self.root)
        self.rename_rule_frame.grid(row=1, column=1, padx=10, pady=5, sticky="ew")

        self.prefix_entry = tk.Entry(self.rename_rule_frame)
        self.prefix_entry.grid(row=0, column=1, padx=5, pady=5, sticky="ew")
        self.prefix_label = tk.Label(self.rename_rule_frame, text="Prefix:")
        self.prefix_label.grid(row=0, column=0, padx=5, pady=5, sticky="ew")

        self.suffix_entry = tk.Entry(self.rename_rule_frame)
        self.suffix_entry.grid(row=1, column=1, padx=5, pady=5, sticky="ew")
        self.suffix_label = tk.Label(self.rename_rule_frame, text="Suffix:")
        self.suffix_label.grid(row=1, column=0, padx=5, pady=5, sticky="ew")

        # Button to apply new names based on the input rules
        self.apply_rename_btn = tk.Button(self.rename_rule_frame, text="Apply Rename", command=self.update_file_lists)
        self.apply_rename_btn.grid(row=2, column=0, columnspan=2, pady=5)


    def add_file_type(self):
        # Logic to add a new file type goes here
        file_type = self.add_file_type_entry.get()
        if file_type and file_type.startswith(".") and file_type not in self.file_type_vars:
            # Assuming self.file_type_vars is a dictionary to track the file types
            human_readable = f"{file_type.upper()} files ({file_type})"
            var = tk.IntVar()
            check = tk.Checkbutton(self.list_frame, text=human_readable, variable=var)
            check.grid(sticky='w')
            self.file_type_vars[file_type] = var
            self.add_file_type_entry.delete(0, tk.END)

    def populate_treeview(self, root_path="."):
        self.tree.delete(*self.tree.get_children())  # Clear existing items
        self.insert_treeview_items('', root_path)

    def insert_treeview_items(self, parent, path):
        for entry in os.listdir(path):
            entry_path = os.path.join(path, entry)
            if os.path.isdir(entry_path):
                node = self.tree.insert(parent, 'end', text=entry, open=False)
                self.insert_treeview_items(node, entry_path)


    def update_file_lists(self, event):
        selected_item = self.tree.focus()  # Get selected directory
        path = self.tree.item(selected_item, 'text')
        # Assuming path is directly the text; may need to adjust based on how paths are stored

        self.original_file_list.delete(0, tk.END)  # Clear ListBoxes
        self.changed_file_list.delete(0, tk.END)

        for file in os.listdir(path):
            self.original_file_list.insert(tk.END, file)
            # Placeholder for changed name logic
            self.changed_file_list.insert(tk.END, self.generate_new_filename(file))

    def generate_new_filename(self, filename):
        prefix = self.prefix_entry.get()
        suffix = self.suffix_entry.get()
        # Splitting filename and extension
        name_part, extension_part = os.path.splitext(filename)
        # Applying prefix and suffix
        new_name = f"{prefix}{name_part}{suffix}{extension_part}"
        return new_name

        return "new_" + filename  # Placeholder implementation

    def apply_rename(self):
        selected_directory = self.tree.focus()  # Get selected directory for rename operation
        path = self.tree.item(selected_directory, 'text')
        # Ensure path handling is consistent with your application's logic

        for file in os.listdir(path):
            original_path = os.path.join(path, file)
            new_name = self.generate_new_filename(file)
            new_path = os.path.join(path, new_name)

            try:
                os.rename(original_path, new_path)
                print(f"Renamed '{original_path}' to '{new_path}'")
            except OSError as e:
                print(f"Error renaming file {file}: {e}")

    # Example of using a message box for feedback
    def show_feedback(self, message, title="Info", type="info"):
        if type == "error":
            messagebox.showerror(title, message)
        elif type == "warning":
            messagebox.showwarning(title, message)
        else:
            messagebox.showinfo(title, message)

  

if __name__ == "__main__":
    root = tk.Tk()
    app = FileRenamerApp(root)
    root.mainloop()


