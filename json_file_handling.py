import json
data = {
"Name": "Alice",
"Age": 25,
"City": "New York"
}
with open("output.json", "w") as file:
    json.dump(data, file, indent=10) # Writes JSON with 4-space indentation

with open("output.json", "r") as fileR:
    data=json.load(fileR)
    print(data)
    print(data["Name"]) # Accessing a value by key  
    print(data.get("Age")) # Accessing a value by key using get() method
    print(data.keys()) # Getting all keys       
    print(data.values()) # Getting all values
    print(data.items()) # Getting all key-value pairs as tuples
