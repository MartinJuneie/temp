import json

# Specify the path to your JSON file
filename = 'temp.json'

try:
    # Open and load the JSON file
    with open(filename, 'r') as file:
        data = json.load(file)
    
    # Pretty-print the JSON data
    print(json.dumps(data, indent=4))

except FileNotFoundError:
    print(f"File '{filename}' not found.")
except json.JSONDecodeError as e:
    print(f"Error decoding JSON: {e}")
