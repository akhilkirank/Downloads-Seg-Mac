# Downloads Organizer

A simple Python utility that automatically organizes your Downloads folder by categorizing files based on their extensions.

## Features

- Automatically sorts files into categorized folders:
  - Images (jpg, jpeg, png, gif, etc.)
  - Documents (doc, docx, pdf, txt, etc.)
  - Audio (mp3, wav, wma, m4a)
  - Video (mp4, avi, mov, flv, wmv)
  - Compressed (zip, rar, tar, gz)
  - Installers (dmg, pkg)
  - Miscellaneous (for all other file types)
- Handles filename conflicts by adding incremental numbers
- Simple, lightweight, and requires no external dependencies

## Usage

Simply run the script:

```
python downloads_organizer.py
```

The script will automatically organize files in your Downloads folder based on their file extensions.

## System Requirements

- Python 3.6 or higher
- macOS/Linux (uses Unix-style paths by default)
- For Windows, you might need to adjust the path variables

## Customization

You can easily customize the file categories by modifying the `file_kinds` dictionary in the script.

## License

MIT License
