import os

def rename_files_in_folder(folder_path, base_name):
    files = os.listdir(folder_path)
    counter = 1

    for file in files:
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            new_file_name = f"{base_name}{counter}{os.path.splitext(file)[1]}"
            new_file_path = os.path.join(folder_path, new_file_name)
            os.rename(file_path, new_file_path)
            counter += 1

if __name__ == "__main__":
    folder_path = input("Enter the folder path: ")
    base_name = input("Enter the base name for the files: ")
    rename_files_in_folder(folder_path, base_name)
    print("Files have been renamed")
