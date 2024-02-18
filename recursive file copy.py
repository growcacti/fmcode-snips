import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import os
import shutil





class FileCopierApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Copier")
        self.root.geometry("400x200")
        self.output = os.getcwd()
        self.setup_widgets()

    def setup_widgets(self):
        # Source directory entry
        self.source_dir_label = tk.Label(self.root, text="Source Directory:")
        self.source_dir_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        
        self.source_dir_entry = tk.Entry(self.root, width=50)
        self.source_dir_entry.grid(row=0, column=1, padx=10, pady=10)
        self.sest_dir_label = tk.Label(self.root, text="sest Directory:")
        self.sest_dir_label.grid(row=6, column=1, padx=10, pady=10, sticky="w")
        
 
        self.dest_dir_entry = tk.Entry(self.root, width=50)
        self.dest_dir_entry.grid(row=7, column=1, padx=10, pady=10)
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_folder)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)
        self.dest_browse_button = tk.Button(self.root, text="Browse", command=self.browse_destination_folder)
        self.dest_browse_button.grid(row=8, column=1, padx=10, pady=10)

        # File extension selection
        self.file_type_label = tk.Label(self.root, text="Select File Type:")
        self.file_type_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        
        self.file_type_combo = ttk.Combobox(self.root, values=[".png", ".py"])
        self.file_type_combo.grid(row=1, column=1, padx=10, pady=10, sticky="ew")
        
        # Start button
        self.start_button = tk.Button(self.root, text="Start Copying", command=self.start_copying)
        self.start_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        
        # Status message
        self.status_message = tk.Label(self.root, text="", fg="green")
        self.status_message.grid(row=3, column=0, columnspan=3, padx=10, pady=10)

    def browse_folder(self):
        folder_selected = filedialog.askdirectory()
        if folder_selected:
            self.source_dir_entry.delete(0, tk.END)
            self.source_dir_entry.insert(0, folder_selected)




    def browse_destination_folder(self):
        destination_folder = self.dest_dir_entry.get()
        folder_selected = filedialog.askdirectory()
        self.output = folder_selected + "/" + destination_folder
        if folder_selected:
            self.dest_dir_entry.delete(0, tk.END)
            self.dest_dir_entry.insert(0, self.output)
            # Ensure the directory exists (create if it does not)
            if not os.path.exists(self.output):
                os.makedirs(self.output)
                messagebox.showinfo("Info", "Destination folder created.")
            else:
                messagebox.showinfo("Info", "Destination folder selected.")


    def copy_files(self, files):
        if not os.path.exists(self.output):
            os.makedirs(self.output)
        
        for file in files:
            shutil.copy(file, self.output)
        return len(files)





    def search_files(self, directory, file_extension):
        files_found = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith(file_extension):
                    files_found.append(os.path.join(root, file))
        return files_found





    def start_copying(self):
        source_dir = self.source_dir_entry.get()
        file_extension = self.file_type_combo.get()
        if not source_dir or not file_extension:
            messagebox.showerror("Error", "Please specify both the source directory and file type.")
            return
        
        try:
            files_to_copy = self.search_files(source_dir, file_extension)
            if files_to_copy:
                num_files_copied = self.copy_files(files_to_copy)
                self.status_message.config(text=f"Successfully copied {num_files_copied} files.", fg="green")
            else:
                self.status_message.config(text="No files found to copy.", fg="red")
        except Exception as e:
            messagebox.showerror("Error", str(e))
            self.status_message.config(text="An error occurred during the copy process.", fg="red")
def main():
    root = tk.Tk()
    app = FileCopierApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

