import os
import shutil
import logging

# Configure logging
logging.basicConfig(
    filename='operations.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def organize_files(folder_path):

    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist!")
            return

        files = os.listdir(folder_path)

        for file in files:

            file_path = os.path.join(folder_path, file)

            # Skip folders
            if os.path.isdir(file_path):
                continue

            # Get file extension
            extension = file.split(".")[-1]

            # Create folder for extension
            extension_folder = os.path.join(folder_path, extension.upper())

            if not os.path.exists(extension_folder):
                os.makedirs(extension_folder)

            # Rename file
            new_name = f"file_{files.index(file)+1}.{extension}"
            new_file_path = os.path.join(extension_folder, new_name)

            # Move and rename
            shutil.move(file_path, new_file_path)

            print(f"Moved: {file} -> {new_name}")

            logging.info(f"Moved {file} to {new_file_path}")

        print("\nFile organization completed successfully!")

    except PermissionError:
        print("Permission denied!")

    except Exception as e:
        print("An error occurred:", e)
        logging.error(f"Error: {e}")

def delete_temp_files(folder_path):

    try:
        for file in os.listdir(folder_path):

            if file.endswith(".tmp") or file.endswith(".log"):

                file_path = os.path.join(folder_path, file)

                os.remove(file_path)

                print(f"Deleted: {file}")

                logging.info(f"Deleted file: {file}")

    except Exception as e:
        print("Error deleting files:", e)
        logging.error(f"Delete Error: {e}")

# Main Program
if __name__ == "__main__":

    print("===== File Organizer Automation =====")

    path = input("Enter folder path: ")

    print("\n1. Organize Files")
    print("2. Delete Temp Files")

    choice = input("Enter your choice: ")

    if choice == "1":
        organize_files(path)

    elif choice == "2":
        delete_temp_files(path)

    else:
        print("Invalid choice!")