import os 
import shutil

open_paths = ["downloads" ,"documents","desktop"] #List used to check validity of path


while True:
    location = input("Enter: (Downloads, Documents, Desktop) ").lower().strip()
    if location in open_paths:
        location = location.capitalize()  # Capitalize the first letter for the directory
        break
    print("Invalid location, Enter again")

directory = os.path.join(os.path.expanduser("~"), location) # Setting the directory 

# Defining extensions and to which foler to sort towards
extensions = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg', '.webp'],
        'Documents': ['.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx', '.txt', '.md'],
        'Archives/Compressed': ['.zip', '.tar', '.gz', '.bz2', '.rar', '.7z'],
        'Audio': ['.mp3', '.wav', '.aac', '.ogg', '.flac'],
        'Video': ['.mp4', '.avi', '.mov', '.mkv', '.webm'],
        'Code': ['.py', '.java', '.cpp', '.c', '.js', '.html', '.css', '.rb', '.php'], # Remeber to work on this as I want to expand and make it better by organising by program files. 
        'Spreadsheets': ['.csv', '.xls', '.xlsx'],
    }

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if os.path.isfile(file_path):
        extension = os.path.splitext(filename)[1].lower()

        folder_name = None
        for folder, exts in extensions.items():
            if extension in exts:
                folder_name = folder
                break
        
        if folder_name is None:
            folder_name = "Others"
        
        folder_path = os.path.join(directory, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        destination = os.path.join(folder_path, filename)
        shutil.move(file_path, destination)
        
        print(f"{filename} has been moved to {folder_name}")
    else:
        print(f"Skipped {filename} as it is a directory and not a file.")

print("Complete")