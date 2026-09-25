import os
import shutil
import tkinter as tk
from tkinter import filedialog

# Select Folder
root = tk.Tk()
root.withdraw()
folder = filedialog.askdirectory()

# File Categories
categories = {

    "Images": [
        ".jpg", ".jpeg", ".png", ".gif", ".bmp",
        ".webp", ".tif", ".tiff", ".svg", ".ico",
        ".heic", ".heif", ".avif", ".raw"
    ],

    "Documents": [
        ".pdf", ".doc", ".docx", ".docm",
        ".txt", ".rtf", ".odt", ".md",
        ".tex", ".epub"
    ],

    "Presentations": [
        ".ppt", ".pptx", ".pptm",
        ".pps", ".ppsx", ".odp"
    ],

    "Spreadsheets": [
        ".xls", ".xlsx", ".xlsm",
        ".csv", ".ods", ".tsv"
    ],

    "Videos": [
        ".mp4", ".mkv", ".avi", ".mov",
        ".wmv", ".flv", ".webm", ".m4v",
        ".3gp", ".mpg", ".mpeg", ".ts",
        ".mts", ".m2ts", ".vob", ".ogv"
    ],

    "Audio": [
        ".mp3", ".wav", ".aac", ".flac",
        ".ogg", ".opus", ".m4a", ".wma",
        ".aiff", ".aif", ".amr", ".alac"
    ],

    "Archives": [
        ".zip", ".rar", ".7z", ".tar",
        ".gz", ".bz2", ".xz", ".tgz"
    ],

}

# Organize Files
for file in os.listdir(folder):

    path = os.path.join(folder, file)

    if os.path.isfile(path):

        extension = os.path.splitext(file)[1].lower()
        category = None

        for name, extensions in categories.items():

            if extension in extensions:
                category = name
                break

        # Move only recognized file types
        if category:

            destination = os.path.join(folder, category)

            os.makedirs(destination, exist_ok=True)

            shutil.move(path, destination)

print("Files organized successfully!")