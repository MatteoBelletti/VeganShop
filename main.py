import json
import os

from program import Program
from warehouse import Warehouse


def check_create_file(file_path):
    directory = os.path.dirname(file_path)

    if not os.path.exists(directory):
        print(f"The directory '{directory}' does not exist. Creating directory...")
        try:
            os.makedirs(directory)
            print(f"The directory '{directory}' has been successfully created.")
        except Exception as e:
            print(f"An error occurred while creating the directory '{directory}':")
            print(e)

    # Check if file exists, if not, create it
    if not os.path.exists(file_path):
        print(f"The file '{file_path}' does not exist. Creating the file...")
        try:
            with open(file_path, 'w') as f:
                print(f"The file '{file_path}' has been successfully created.")
                json.dump(list(), f)
                print(f"The file '{file_path}' has been successfully initializated.")
        except Exception as e:
            print(f"An error occurred while creating the file '{file_path}':")
            print(e)
    else:
        print(f"The file '{file_path}' already exists.")


def main():
    check_create_file("./db/warehouse_db.json")
    warehouse = Warehouse("./db/warehouse_db.json")
    program = Program(warehouse)
    program.start()


if __name__ == "__main__":
    main()
