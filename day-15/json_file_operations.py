# json file operations 
json_data = {
    "name": "Swapnil",
    "age": 22,
    "skills": ["Python", "SQL", "React"]
}
# Writing JSON file
with open("data.json", "w") as file:
    json.dump(json_data, file, indent=4)
# Reading JSON file
with open("data.json", "r") as file:
    data = json.load(file)
print("JSON File Content:")
print(data)
print("Access Name:", data["name"])