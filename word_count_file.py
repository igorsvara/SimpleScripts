def word_count_file():
    file_path = input("Enter the path of the file to count words: ")
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            words = content.split()
            word_count = len(words)
            print(f"The file contains {word_count} words.")
    except FileNotFoundError:
        print("Error: File not found.")
    except PermissionError:
        print("Error: Permission denied. Check read permissions for the file.")


word_count_file()

