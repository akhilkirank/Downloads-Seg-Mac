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

misc_folder_path = downloads_path + "Miscellaneous"
if not os.path.exists(misc_folder_path):
    os.makedirs(misc_folder_path)

for file_name in os.listdir(downloads_path):
    if os.path.isfile(downloads_path + file_name):
        file_type = file_name.split(".")[-1]
        moved = False
        for kind, types in file_kinds.items():
            if file_type.lower() in types:
                new_folder_path = downloads_path + kind
                if not os.path.exists(new_folder_path):
                    os.makedirs(new_folder_path)
                old_file_path = downloads_path + file_name
                new_file_path = new_folder_path + "/" + file_name
                move(old_file_path, new_file_path)
                moved = True
        if not moved:
            old_file_path = downloads_path + file_name
            new_file_path = misc_folder_path + "/" + file_name
            move(old_file_path, new_file_path)
