# Example 1
import subprocess

def subprocess_example(command):
    try:
        # Run a command and get output
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        print("Command Output:")
        print(result.stdout)
        print("Command Error (if any):")
        print(result.stderr)
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
subprocess_example('ls -l')

# Example 2
import os

def os_example():
    try:
        # Get the current working directory
        cwd = os.getcwd()
        print(f"Current Working Directory: {cwd}")

        # List files in the current directory
        files = os.listdir(cwd)
        print("Files in Directory:")
        for file in files:
            print(file)

        # Create a new directory
        new_dir = 'new_directory'
        os.mkdir(new_dir)
        print(f"Directory '{new_dir}' created")

        # Remove the directory
        os.rmdir(new_dir)
        print(f"Directory '{new_dir}' removed")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
os_example()
