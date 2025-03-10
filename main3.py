import os
from shutil import move

downloads_path = os.path.expanduser("~") + "/Downloads/"

file_kinds = {
    "Images": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "ico"],
    "Documents": ["doc", "docx", "pdf", "txt", "rtf"],
    "Audio": ["mp3", "wav", "wma", "m4a"],
    "Video": ["mp4", "avi", "mov", "flv", "wmv"],
    "Compressed": ["zip", "rar", "tar", "gz"],
    "Installers": ["dmg", "pkg"]
}

misc_folder_path = os.path.join(downloads_path, "Miscellaneous")
os.makedirs(misc_folder_path, exist_ok=True)

for file_name in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, file_name)
    if os.path.isfile(file_path):
        file_type = file_name.split(".")[-1].lower()
        moved = False
        for kind, types in file_kinds.items():
            if file_type in types:
                new_folder_path = os.path.join(downloads_path, kind)
                os.makedirs(new_folder_path, exist_ok=True)
                new_file_path = os.path.join(new_folder_path, file_name)
                if os.path.exists(new_file_path):
                    base_name, extension = os.path.splitext(file_name)
                    i = 1
                    while os.path.exists(new_file_path):
                        new_file_name = f"{base_name}_{i}{extension}"
                        new_file_path = os.path.join(new_folder_path, new_file_name)
                        i += 1
                move(file_path, new_file_path)
                moved = True
                break
        if not moved:
            new_file_path = os.path.join(misc_folder_path, file_name)
            if os.path.exists(new_file_path):
                base_name, extension = os.path.splitext(file_name)
                i = 1
                while os.path.exists(new_file_path):
                    new_file_name = f"{base_name}_{i}{extension}"
                    new_file_path = os.path.join(misc_folder_path, new_file_name)
                    i += 1
            move(file_path, new_file_path)