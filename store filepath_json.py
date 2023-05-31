import json

# Function to save the file path to a configuration file
def save_file_path(file_path):
    config = {"file_path": file_path}
    with open("config.json", "w") as file:
        json.dump(config, file)

# Function to retrieve the file path from the configuration file
def load_file_path():
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
            return config["file_path"]
    except FileNotFoundError:
        return None

# Example usage
file_path = "path/to/your/file.txt"  # Replace with the actual file path

# Save the file path
save_file_path(file_path)

# Retrieve the file path
loaded_file_path = load_file_path()
if loaded_file_path:
    print("File path:", loaded_file_path)
else:
    print("No file path found in the configuration file.")
