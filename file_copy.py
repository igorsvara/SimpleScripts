import shutil


def file_copy():
    source_file = input("Enter the source file path: ")
    destination_folder = input("Enter the destination folder path: ")

    try:
        shutil.copy(source_file, destination_folder)
        print("File copied successfully.")
    except FileNotFoundError:
        print("Error: Source file not found.")
    except IsADirectoryError:
        print("Error: Destination should be a folder.")
    except PermissionError:
        print("Error: Permission denied. Check write permissions in the destination folder.")


file_copy()
