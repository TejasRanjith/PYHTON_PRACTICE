import os

def get_largest_folder(path='.'):
    folders = [f for f in os.listdir(path) if os.path.isdir(os.path.join(path, f))]
    if not folders:
        return None, 0

    largest_folder = max(folders, key=lambda f: os.path.getsize(os.path.join(path, f)))
    folder_size = os.path.getsize(os.path.join(path, largest_folder))
    
    return largest_folder, folder_size

# Provide the path to the directory you want to search
directory_path = 'C:/Users/home'
largest_folder_name, largest_folder_size = get_largest_folder(directory_path)

largest_folder_name, largest_folder_size
