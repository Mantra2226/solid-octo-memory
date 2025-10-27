# Program: Read a file provided by the user and handle file errors

def read_file():
    # Ask the user for the filename
    filename = input("Enter the name of the file to read: ")

    try:
        # Try opening and reading the file
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read()
            print("\n--- File Content ---")
            print(content)
            print("--------------------")

    except FileNotFoundError:
        print(f"❌ Error: The file '{filename}' was not found.")
    except PermissionError:
        print(f"⚠️ Error: You don’t have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"⚠️ An unexpected error occurred: {e}")

# Run the function
if __name__ == "__main__":
    read_file()
