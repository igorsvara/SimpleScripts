def line_count_file():
    file_path = input("Enter the path of the file to count lines: ")
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            line_count = len(lines)
            print(f"The file contains {line_count} lines.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied. Check read permissions for the file.")


line_count_file()
