import csv
import json
# text file operations 
# Writing txt file
with open("sample.txt", "w") as file:
    file.write("Hello Swapnil\n")
    file.write("Learning Python File Handling\n")
# Appending to text file
with open("sample.txt", "a") as file:
    file.write("This is appended line.\n")
# Reading text file
with open("sample.txt", "r") as file:
    content = file.read()
    print("TXT File Content:\n", content)
# csv file operations 
csv_data = [
    ["Name", "Age"],
    ["Swapnil", 22],
    ["Rahul", 25]
]
# Writing to CSV file
with open("data.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerows(csv_data)

# Reading CSV file
with open("data.csv", "r") as file:
    reader = csv.reader(file)
    print("CSV File Content:")
    for row in reader:
        print(row)
# json file operations 
print("------ JSON FILE OPERATIONS ------")

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