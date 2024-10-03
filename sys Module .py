# Example 1
import sys

def sys_example():
    # Print Python version
    print("Python version:", sys.version)

    # Print command line arguments
    print("Command line arguments:", sys.argv)

    # Exit the program
    if len(sys.argv) != 2:
        print("Usage: python script.py <name>")
        sys.exit(1)

    name = sys.argv[1]
    print(f"Hello, {name}!")

if __name__ == "__main__":
    sys_example()

# Example 2
import os

def os_example():
    # Get the current working directory
    cwd = os.getcwd()
    print("Current Working Directory:", cwd)

    # List files in the current directory
    files = os.listdir(cwd)
    print("Files in Directory:")
    for file in files:
        print(file)

    # Create a new directory
    new_dir = 'test_directory'
    os.makedirs(new_dir, exist_ok=True)
    print(f"Directory '{new_dir}' created")

    # Remove the directory
    os.rmdir(new_dir)
    print(f"Directory '{new_dir}' removed")

if __name__ == "__main__":
    os_example()

# Example 3
import pickle

def pickle_example():
    data = {'name': 'John', 'age': 30, 'city': 'New York'}

    # Serialize data to a file
    with open('data.pkl', 'wb') as file:
        pickle.dump(data, file)

    # Deserialize data from the file
    with open('data.pkl', 'rb') as file:
        loaded_data = pickle.load(file)

    print("Loaded Data:", loaded_data)

if __name__ == "__main__":
    pickle_example()

# Example 4
python
Copy code
import json

def json_example():
    data = {'name': 'Jane', 'age': 25, 'city': 'London'}

    # Serialize data to a JSON file
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

    # Deserialize data from the JSON file
    with open('data.json', 'r') as file:
        loaded_data = json.load(file)

    print("Loaded Data:", loaded_data)

if __name__ == "__main__":
    json_example()

# Example 5
import time

def time_example():
    # Get the current time
    current_time = time.time()
    print("Current Time (epoch):", current_time)

    # Sleep for 2 seconds
    print("Sleeping for 2 seconds...")
    time.sleep(2)
    print("Awoke!")

if __name__ == "__main__":
    time_example()

# Example 6
from datetime import datetime, timedelta

def datetime_example():
    # Get current date and time
    now = datetime.now()
    print("Current Date and Time:", now)

    # Format date and time
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")
    print("Formatted Date and Time:", formatted)

    # Add 5 days to the current date
    future_date = now + timedelta(days=5)
    print("Future Date (after 5 days):", future_date)

if __name__ == "__main__":
    datetime_example()

# Example 7
def file_handling_example():
    filename = 'sample.txt'

    # Write to a file
    with open(filename, 'w') as file:
        file.write('Hello, world!\n')
        file.write('Welcome to Python file handling.')

    # Read from a file
    with open(filename, 'r') as file:
        content = file.read()
        print("File Content:")
        print(content)

if __name__ == "__main__":
    file_handling_example()

# Example 8
import logging

def logging_example():
    # Configure the logger
    logging.basicConfig(filename='example.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

    # Log some messages
    logging.debug('This is a debug message')
    logging.info('This is an info message')
    logging.warning('This is a warning message')
    logging.error('This is an error message')
    logging.critical('This is a critical message')

if __name__ == "__main__":
    logging_example()

# Example 9
import re

def re_example():
    text = "The price of the product is $25.99 and the discount is 10%."

    # Find all prices
    prices = re.findall(r'\$\d+\.\d+', text)
    print("Prices found:", prices)

    # Replace price with a new value
    updated_text = re.sub(r'\$\d+\.\d+', '$29.99', text)
    print("Updated Text:", updated_text)

if __name__ == "__main__":
    re_example()

# Example 10
import numpy as np

def numpy_example():
    # Create a numpy array
    array = np.array([1, 2, 3, 4, 5])
    print("Numpy Array:", array)

    # Perform basic operations
    array_squared = np.square(array)
    print("Squared Array:", array_squared)

    # Calculate mean
    mean_value = np.mean(array)
    print("Mean Value:", mean_value)

if __name__ == "__main__":
    numpy_example()

# Example 11
import pandas as pd

def pandas_example():
    # Create a DataFrame
    data = {
        'Name': ['Alice', 'Bob', 'Charlie'],
        'Age': [25, 30, 35],
        'City': ['New York', 'Los Angeles', 'Chicago']
    }
    df = pd.DataFrame(data)
    print("DataFrame:")
    print(df)

    # Access specific columns
    print("\nNames:")
    print(df['Name'])

    # Filter rows
    filtered_df = df[df['Age'] > 30]
    print("\nFiltered DataFrame (Age > 30):")
    print(filtered_df)

if __name__ == "__main__":
    pandas_example()

