import os
import shutil

username = 'akhilkirank'
downloads_path = f'/Users/{username}/Downloads'

for dirpath, dirnames, filenames in os.walk(downloads_path):
    for filename in filenames:
        file_path = os.path.join(dirpath, filename)
        if os.path.isfile(file_path):
            dst_path = os.path.join(downloads_path, filename)
            if os.path.exists(dst_path):
                os.remove(dst_path)
            if os.path.exists(file_path):
                shutil.move(file_path, downloads_path)
