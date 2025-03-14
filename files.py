import os

def create_file_if_not_exists(filename):
    """Creates a file if it doesn't exist and prompts the user to add content."""
    if not os.path.exists(filename):
        print(f"🔹 The file '{filename}' does not exist. Let's create it!")
        with open(filename, "w") as file:
            content = input("Enter content for the new file: ")
            file.write(content + "\n")
        print(f"✅ File '{filename}' created successfully!\n")

def read_file():
    """Reads and prints the contents of the file."""
    filename = input("Enter the filename to read: ")

    # Ensure the file exists before reading
    create_file_if_not_exists(filename)

    try:
        # Open and read the file
        with open(filename, "r") as file:
            content = file.read()
            print("\n📖 File Content:")
            print(content)
    except PermissionError:
        print("❌ Error: You do not have permission to access this file.")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# Run the function
read_file()
