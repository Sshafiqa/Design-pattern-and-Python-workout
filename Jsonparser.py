import json

# Data to be serialized
data = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "is_student": False,
    "courses": ["Python", "JavaScript"]
}

# Serialize to string
json_str = json.dumps(data, indent=4)
print("JSON String:\n", json_str)

# Serialize to file
with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

# Deserialize from file
with open('data.json', 'r') as file:
    data_loaded = json.load(file)
    print("Data Loaded from File:\n", data_loaded)

# Deserialize from string
data_from_str = json.loads(json_str)
print("Data Loaded from String:\n", data_from_str)
