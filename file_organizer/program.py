import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox

extension_folders = {
    "pdf": "PDFs",
    "txt": "Text_Documents",
    "jpg": "Images",
    "png": "Images",
    "docx": "Word_Documents"
}

def organize_files():
    path_folder = filedialog.askdirectory(title="Select Folder to Organize")
    if not path_folder:
        return
    
    for file in os.listdir(path_folder):
        if os.path.isfile(os.path.join(path_folder, file)):
            extension = os.path.splitext(file)[1][1:].lower()
            folder_name = extension_folders.get(extension, "Other")  # Unknown files go to "Other"

            src_path = os.path.join(path_folder, file)
            dest_folder = os.path.join(path_folder, folder_name)
            dest_path = os.path.join(dest_folder, file)

            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(src_path, dest_path)
    
    messagebox.showinfo("Done!", f"Files in '{path_folder}' have been organized!")

root = tk.Tk()
root.title("File Organizer Tool")
root.geometry("400x150")

label = tk.Label(root, text="Organize files by type with one click", font=("Arial", 12))
label.pack(pady=10)

btn = tk.Button(root, text="Select Folder to Organize", command=organize_files, width=25, height=2)
btn.pack(pady=20)

root.mainloop()
