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

# Create Miscellaneous folder
misc_folder_path = downloads_path + "Miscellaneous"
if not os.path.exists(misc_folder_path):
    os.makedirs(misc_folder_path)

# Create Folders directory for storing folders
folders_path = downloads_path + "Folders"
if not os.path.exists(folders_path):
    os.makedirs(folders_path)

for item_name in os.listdir(downloads_path):
    item_path = os.path.join(downloads_path, item_name)
    
    # Handle folders
    if os.path.isdir(item_path):
        # Skip the organization folders we created
        if item_name not in ["Miscellaneous", "Folders"] + list(file_kinds.keys()):
            new_folder_path = os.path.join(folders_path, item_name)
            # Handle case where folder with same name exists
            if os.path.exists(new_folder_path):
                counter = 1
                while os.path.exists(new_folder_path + f" ({counter})"):
                    counter += 1
                new_folder_path += f" ({counter})"
            move(item_path, new_folder_path)
    
    # Handle files
    elif os.path.isfile(item_path):
        file_type = item_name.split(".")[-1] if "." in item_name else ""
        moved = False
        for kind, types in file_kinds.items():
            if file_type.lower() in types:
                new_folder_path = downloads_path + kind
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)
                new_file_path = os.path.join(new_folder_path, item_name)
                # Handle case where file with same name exists
                if os.path.exists(new_file_path):
                    counter = 1
                    base_name, extension = os.path.splitext(item_name)
                    while os.path.exists(os.path.join(new_folder_path, f"{base_name} ({counter}){extension}")):
                        counter += 1
                    new_file_path = os.path.join(new_folder_path, f"{base_name} ({counter}){extension}")
                move(item_path, new_file_path)
                moved = True
                break
        if not moved:
            new_file_path = os.path.join(misc_folder_path, item_name)
            # Handle case where file with same name exists
            if os.path.exists(new_file_path):
                counter = 1
                base_name, extension = os.path.splitext(item_name)
                while os.path.exists(os.path.join(misc_folder_path, f"{base_name} ({counter}){extension}")):
                    counter += 1
                new_file_path = os.path.join(misc_folder_path, f"{base_name} ({counter}){extension}")
            move(item_path, new_file_path)