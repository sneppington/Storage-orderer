#Download_manager
import os
import shutil
from pathlib import Path

script_dir = os.path.dirname(os.path.realpath(__file__))

home_dir = Path.home()
downloads_folder = os.path.join(home_dir, "Downloads")



def create_folder(directory):
    """Create a folder at the specified directory."""
    try:
        os.makedirs(directory)
        print(f"Folder '{directory}' created successfully.")
    except FileExistsError:
        print(f"Folder '{directory}' already exists.")
    except Exception as e:
        print(f"Error occurred while creating folder '{directory}': {e}")

def move_files(directory):
    
    if not os.path.exists(directory):
        print("Error: No such directory\nType it again:")
        move_files(input())
        return
    
    files = os.listdir(directory)
    
    for filename in files:
        
        extension = os.path.splitext(filename)[1] or "Unclassifiable"
        
        source_path = os.path.join(directory, filename)
        destination_path = os.path.join(script_dir + r"\Archive/{0}".format(extension), filename)
        
        try:
            shutil.move(source_path, destination_path)
        except Exception:
            create_folder(script_dir + r"\Archive/{0}".format(extension))
            shutil.move(source_path, destination_path)
        
        
        
        print(f"Moved {filename} to " + script_dir + r"\Archive/{0}".format(extension))



def main():
    print("Mode: ['downloads' 'other']")
    answer = input().lower()
    
    if answer == "downloads":
        move_files(downloads_folder)
    elif answer == "other":
        print("Directory:")
        directory = input()
        move_files(directory)
    else:
        print("Error: No such mode")
        main()
        return



main()
input()