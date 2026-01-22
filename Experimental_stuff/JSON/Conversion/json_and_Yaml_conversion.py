import json
import yaml

# Sample data
data = {
    "name": "John Doe",
    "age": 30,
    "roles": ["admin", "user"],
    "address": {
        "city": "New York",
        "zipCode": "10001"
    }
}

# JSON to YAML
json_string = json.dumps(data, indent=2)
print("JSON:")
print(json_string)

yaml_string = yaml.dump(data, default_flow_style=False)
print("\nYAML:")
print(yaml_string)

# YAML to JSON
yaml_input = """
name: Jane Smith
age: 25
active: true
"""

data_from_yaml = yaml.safe_load(yaml_input)
json_from_yaml = json.dumps(data_from_yaml, indent=2)
print("YAML to JSON:")
print(json_from_yaml)