
import os

def create_file(file_path):
    try:
        with open(file_path, "w"):
            print("File created successfully")

    except OSError:
        print("Error caretion in file")


def write_to_file(file_path):
    try:
        with open(file_path, 'w') as file:
            print("Enter the content to write to the file (Press 'q' key to terminate):")
            while True:
                content = input()
                # if content:
                #     file.write(content + "\n")
                if content.lower() == 'q':
                    break
                file.seek(0)  # Move the file pointer to the beginning
                file.truncate()  # Clear the file content
                file.write(content)

        print("Content written to file successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred while writing to the file:", str(e))


def append_to_file(file_path):
    try:
        with open(file_path, 'a') as file:
            print("Enter the content to append to the file (Press 'q' to terminate):")
            while True:
                content = input()
                if content.lower() == 'q':
                    break
                file.write(content + "\n")

        print("Content appended to file successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred while appending to the file:", str(e))

# method to read file


def read_file(file_path):
    try:
        with open(file_path, 'r') as file:
            print(file.read())
            print("file read successfully")

    except FileNotFoundError:
        print("File not found.")

# delete file


def delete_file(file_path):
    try:
        os.remove(file_path)
        print("File deleted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred while deleting the file:", str(e))


# Example usage

# create main proram from here

while True:
    print("======= File Manager ======")
    print("1. Create a file")
    print("2. write to a file")
    print("3. Edit file")
    print("4. Read a file")
    print("5. Delete a file")
    print("6. Exit ")

    choice = input("Enter your choice")

    if choice == '1':
        file_path = input(">>Enter file path:")
        # call the create_file method
        create_file(file_path)

    if choice == '2':
        file_path = input(">>Enter file path:")
        # call wirte to the file function
        write_to_file(file_path)

    if choice == '3':
        file_path = input(">>Enter the file path: ")
        append_to_file(file_path)

    if choice == '4':
        file_path = input(">>Enter the file path: ")
        read_file(file_path)

    if choice == '5':
        file_path = input(">>Enter the file path")
        delete_file(file_path)

    if choice == '6':
        # exit the programe
        print("Thank you for using the file manager")
        break
    else:
        print("Invalid choice . Please try again")
