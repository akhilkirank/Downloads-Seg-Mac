#!/usr/bin/env python3
"""
Downloads Organizer - A utility to automatically organize files in your Downloads folder
by categorizing them based on file extensions.
"""

import os
import shutil
from pathlib import Path

def organize_downloads():
    """Organize files in the Downloads folder based on their file extensions."""
    # Get the downloads path using pathlib for better cross-platform compatibility
    downloads_path = Path.home() / "Downloads"
    
    # Dictionary mapping categories to their respective file extensions
    file_categories = {
        "Images": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "ico", "svg", "webp"],
        "Documents": ["doc", "docx", "pdf", "txt", "rtf", "xls", "xlsx", "ppt", "pptx", "csv"],
        "Audio": ["mp3", "wav", "wma", "m4a", "flac", "aac", "ogg"],
        "Video": ["mp4", "avi", "mov", "flv", "wmv", "mkv", "webm"],
        "Compressed": ["zip", "rar", "tar", "gz", "7z", "bz2"],
        "Installers": ["dmg", "pkg", "deb", "rpm", "msi", "exe"],
        "Code": ["py", "js", "html", "css", "java", "c", "cpp", "h", "json", "xml", "md"]
    }
    
    # Create a Miscellaneous folder for uncategorized files
    misc_folder_path = downloads_path / "Miscellaneous"
    misc_folder_path.mkdir(exist_ok=True)
    
    # Process each file in the downloads directory
    for item in downloads_path.iterdir():
        # Skip directories and the script itself
        if item.is_dir() or item.name == os.path.basename(__file__):
            continue
        
        # Get the file extension (without the dot)
        file_extension = item.suffix.lower().lstrip('.')
        
        # Try to categorize the file
        categorized = False
        for category, extensions in file_categories.items():
            if file_extension in extensions:
                # Create category folder if it doesn't exist
                category_folder = downloads_path / category
                category_folder.mkdir(exist_ok=True)
                
                # Determine the destination path, handling name conflicts
                dest_path = category_folder / item.name
                if dest_path.exists():
                    base_name = item.stem
                    i = 1
                    while (category_folder / f"{base_name}_{i}{item.suffix}").exists():
                        i += 1
                    dest_path = category_folder / f"{base_name}_{i}{item.suffix}"
                
                # Move the file
                try:
                    shutil.move(str(item), str(dest_path))
                    print(f"Moved {item.name} to {category} folder")
                    categorized = True
                    break
                except Exception as e:
                    print(f"Error moving {item.name}: {e}")
        
        # If file wasn't categorized, move it to Miscellaneous
        if not categorized:
            dest_path = misc_folder_path / item.name
            if dest_path.exists():
                base_name = item.stem
                i = 1
                while (misc_folder_path / f"{base_name}_{i}{item.suffix}").exists():
                    i += 1
                dest_path = misc_folder_path / f"{base_name}_{i}{item.suffix}"
            
            try:
                shutil.move(str(item), str(dest_path))
                print(f"Moved {item.name} to Miscellaneous folder")
            except Exception as e:
                print(f"Error moving {item.name}: {e}")

if __name__ == "__main__":
    print("Starting Downloads folder organization...")
    organize_downloads()
    print("Organization complete!") 