# File Organizer GUI in Python

A simple Python GUI utility that organizes files in a selected folder into separate categories based on their file extensions.

The project uses Tkinter for folder selection and Python's file-system modules to automatically move files into organized category folders.

## 🎥 Preview

[▶️ Watch Project Demo](./Preview/File%20Organizer%20By%20Gui.mp4)

The preview demonstrates selecting a folder and automatically organizing its files into categories such as Images, Documents, Archives, and other supported file types.

## ✨ Features

- Select a folder using a graphical folder-selection dialog
- Automatically identify files by their extensions
- Organize files into category folders
- Supports images
- Supports documents
- Supports presentations
- Supports spreadsheets
- Supports videos
- Supports audio files
- Supports archives
- Automatically creates required category folders
- Moves files into their corresponding categories
- Displays a successful completion message in the terminal

## 🎯 Project Overview

The File Organizer GUI is a Python utility designed to reduce clutter in folders by automatically grouping files according to their file extensions.

The user selects a folder through a Tkinter file-dialog interface. The program then checks the files inside the selected folder, identifies their extensions, creates the appropriate category folders, and moves the files into those folders.

## 🔄 How It Works

    1. The program imports the required Python modules.
    2. Tkinter opens a folder-selection dialog.
    3. The user selects the folder that needs to be organized.
    4. File categories and their supported extensions are defined.
    5. The program scans the selected folder.
    6. Each file extension is checked against the configured categories.
    7. The corresponding category folder is created when required.
    8. The file is moved into its category folder.
    9. The program finishes after processing the selected folder.

## 📂 Supported File Categories

The project defines categories based on file extensions.

| Category | Example Extensions |
|---|---|
| Images | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.webp`, `.tif`, `.tiff`, `.svg`, `.ico`, `.heic`, `.heif`, `.avif`, `.raw` |
| Documents | `.pdf`, `.doc`, `.docx`, `.docm`, `.txt`, `.rtf`, `.odt`, `.md`, `.tex`, `.epub` |
| Presentations | `.ppt`, `.pptx`, `.pptm`, `.pps`, `.ppsx`, `.odp` |
| Spreadsheets | `.xls`, `.xlsx`, `.xlsm`, `.csv`, `.ods`, `.tsv` |
| Videos | `.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`, `.webm`, `.m4v`, `.3gp`, `.mpg`, `.mpeg`, `.ts`, `.mts`, `.m2ts`, `.vob`, `.ogv` |
| Audio | `.mp3`, `.wav`, `.aac`, `.flac`, `.ogg`, `.opus`, `.m4a`, `.wma`, `.aiff`, `.aif`, `.amr`, `.alac` |

## 🖥️ Graphical Interface

The project uses Tkinter's directory-selection dialog to allow the user to choose the folder that should be organized.

The GUI interaction is intentionally simple:

    Open Application
          ↓
    Select Folder
          ↓
    Scan Files
          ↓
    Identify Extensions
          ↓
    Create Category Folders
          ↓
    Move Files
          ↓
    Files Organized

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Tkinter | Graphical folder-selection interface |
| `filedialog` | Selecting the folder to organize |
| `os` | File-system operations |
| `shutil` | Moving files between folders |

## 📁 Project Structure

    File-Organizer-GUI-in-Python/
    │
    ├── Preview_video/
    │   └── File Organizer By Gui.mp4
    │
    ├── main.py
    │
    └── README.md

## ▶️ Run Locally

### 1. Clone the Repository

    git clone https://github.com/dheerajmishra75/File-Organizer-GUI-in-Python.git

### 2. Navigate to the Project

    cd File-Organizer-GUI-in-Python

### 3. Run the Application

    python main.py

A folder-selection dialog will open and you can select the folder that you want to organize.

## 🧪 Example Workflow

    Selected Folder
          ↓
    ├── image.png
    ├── document.pdf
    ├── presentation.pptx
    ├── data.xlsx
    └── video.mp4

    After Organization

    Selected Folder
    ├── Images
    │   └── image.png
    ├── Documents
    │   └── document.pdf
    ├── Presentations
    │   └── presentation.pptx
    ├── Spreadsheets
    │   └── data.xlsx
    └── Videos
        └── video.mp4

## 📚 Python Concepts Practiced

- File and directory handling
- File extensions
- Dictionaries
- Lists
- Loops
- Conditional statements
- Functions
- Tkinter
- File dialogs
- `os` module
- `shutil` module
- Basic automation

## 🎯 Learning Outcomes

Through this project, I practiced how to:

- Work with files and directories using Python
- Build a simple GUI interaction using Tkinter
- Select folders programmatically
- Identify files using their extensions
- Create directories automatically
- Move files using `shutil`
- Automate repetitive file-management tasks
- Organize application logic using Python data structures

## 🚀 Future Improvements

Possible improvements for future versions include:

- Add a graphical progress indicator
- Add a preview before moving files
- Add duplicate-file handling
- Add custom categories
- Allow users to configure extensions
- Add an undo operation
- Add a completion summary
- Handle unsupported file types separately
- Add a fully graphical interface

## 🔗 Project Links

- GitHub: https://github.com/dheerajmishra75/File-Organizer-GUI-in-Python

## 👨‍💻 Author

**Dheeraj Mishra**

B.Tech CSE Student | Python | Data Science | Machine Learning | Backend Development

## 📌 Disclaimer

This project was created for learning and practice purposes. Since the application moves files automatically, users should test it on non-critical folders before using it with important files.
