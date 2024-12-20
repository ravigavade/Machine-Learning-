import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: /")

# List all files and directories in the current directory
files_and_dirs = os.listdir(current_directory)

# Print only files
print("Files in the current directory:")
for item in files_and_dirs:
    if os.path.isfile(item):  # Check if it's a file
        print(item)
