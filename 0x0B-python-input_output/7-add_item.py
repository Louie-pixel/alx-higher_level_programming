#!/usr/bin/python3
"""
Adds all arguments to a Python list and then saves them to a file.
"""

import sys
import os.path
from json import dump, load
from save_to_json_file import save_to_json_file
from load_from_json_file import load_from_json_file

if __name__ == "__main__":
    file_name = "add_item.json"
    
    # Check if file exists
    if os.path.exists(file_name):
        # Load existing data from file
        with open(file_name, "r") as f:
            data = load(f)
    else:
        data = []

    # Append command line arguments to the data list
    data.extend(sys.argv[1:])

    # Save the updated list to the file
    with open(file_name, "w") as f:
        dump(data, f)
