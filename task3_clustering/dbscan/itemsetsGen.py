import json

# Read the content of the file
with open('instacart.json', 'r') as file:
    content = file.read()

# Split the content into individual JSON objects
json_objects = content.split('\n')

# Initialize an empty list to store the extracted items
items_list = []

# Iterate through each JSON object and extract the "items" field
for json_str in json_objects:
    try:
        # Load the JSON object
        json_obj = json.loads(json_str)

        # Extract the "items" field and append it to the list
        items_list.append(json_obj['items'])

    except json.JSONDecodeError as e:
        pass

items_list = [[int(float(num)) for num in sublist] for sublist in items_list]

# Print the final list of items
print(items_list[-10:])

output_file_path = 'instacartItemsets.txt'

# Save the list to a text file
with open(output_file_path, 'w') as file:
    for sublist in items_list:
        file.write(','.join(map(str, sublist)) + '\n')