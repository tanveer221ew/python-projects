import os
import shutil

path_folder = r"C:\Users\Tanveer\Desktop\testfolder"
extension_folders = {
    "pdf": "PDFs",
    "txt": "Text_Documents",
    "jpg": "Images",  
    "png": "Images",
    "docx": "Word_Documents"
}

for file in os.listdir(path_folder):
    extension = os.path.splitext(file)[1][1:].lower()  
    folder_name = extension_folders.get(extension)     

    if folder_name:
        src_path = os.path.join(path_folder, file)
        dest_folder = os.path.join(path_folder, folder_name)
        dest_path = os.path.join(dest_folder, file)

        os.makedirs(dest_folder, exist_ok=True)
        shutil.move(src_path, dest_path)
