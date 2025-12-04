"""
This is a script that helps to organize files into the appropriate categories as specified
"""

import os
import shutil

# Define the dictionary for file type categories

FILE_SCHEMA = {
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx", ".rtf", ".odt", ".ods", ".odp", ".csv"],
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".tiff", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".mpeg", ".mpg"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg", ".wma", ".m4a"],
    "Compressed_files": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code_files": [".json", ".xml", ".py", ".js", ".ts", ".html", ".css", ".yaml", ".yml", ".c", ".cpp", ".cs", ".java", ".rb", ".php", ".swift", ".go"],
    "Executables": [".exe", ".msi", ".bat", ".cmd", ".ps1"],
    "Security_key": [".asc", ".pem", ".key", ".crt", ".csr"],
    "Configs": [".ini", ".cfg", ".conf", ".reg", ".env"],
    "Databases": [".db", ".sqlite", ".sql", ".accdb", ".mdb"],
    "Backups": [".bak", ".hive", ".old"],
    "Design_files": [".psd", ".ai", ".xd", ".fig", ".sketch"],
    "Others": []
}

def file_organizer(directory):
    """Organizes files in the given directory by their file types"""
    if not os.path.isdir(directory):
        print(f"Error: {directory}is not a valid directory.")
        return
    
    # Create folders for each category if not exist
    for category in FILE_SCHEMA:
        folder_path = os.path.join(directory, category)
        os.makedirs(folder_path, exist_ok=True)

    # Move files into appropriate folders
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Check file extension and move to corresponding folder
        
        file_moved = False
        for category, extensions in FILE_SCHEMA.items():
            if any(filename.lower().endswith(ext) for ext in extensions):
                shutil.move(file_path, os.path.join(directory, category, filename))
                file_moved = True
                break

        # Move to "Others" if no match
        if not file_moved:
            shutil.move(file_path, os.path.join(directory, "others", filename))

            print(f"Files in '{directory}' have been organized succesfully!")

organize_directory = input("Enter the directory file path to organize: ")

file_organizer(organize_directory)



