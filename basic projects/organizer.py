import os
import shutil
folder_path = '/Users/home/Downloads'
file_types = {
    "images" : [".jpg",".png",".jpeg"],
    "documents" : [".txt",".pdf",".docx"],
    "Music": [".mp3"],
    "Videos": [".mp4"],
    "Code": [".py", ".c", ".cpp", ".java"]
}
files = os.listdir(folder_path)
for file in os.listdir(folder_path):
    file_path = os.path.join(folder_path, file)

    if os.path.isfile(file_path):
        name, ext = os.path.splitext(file)

        for folder, extensions in file_types.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(folder_path, folder)
                os.makedirs(target_folder, exist_ok=True)
                shutil.move(file_path, target_folder)
                break