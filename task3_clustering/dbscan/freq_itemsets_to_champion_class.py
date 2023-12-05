from collections import Counter
import pickle
import json

freq_items = []

# Open the text file for reading.
with open('leagueItemsets.txt', 'r') as file:
    # Iterate through each line in the file.
    for line in file:
        # Split the line by ',' to separate key and items.
        parts = line.strip().split(',')
        
        # The remaining elements are items converted to integers and stored in a list.
        items = [int(float(x)) for x in parts]
        
        # Add the key-value pair to the list.
        freq_items.append(items)

item_class_mapping = {}

# Open the item_class.txt file for reading.
with open('item_class.txt', 'r') as file:
    item_class_mapping = json.load(file)

# Now, item_class_mapping contains the mapping of item_id to championClass.

def majority_champion_class(items):
    champion_class_count = Counter([item_class_mapping[str(item)] for item in items if str(item) in item_class_mapping])
    most_common = champion_class_count.most_common(1)
    return most_common[0][0] if most_common else None

# Create a new dictionary with the majority championClass for each list.
freq_items_to_champion_class = {tuple(items): majority_champion_class(items) for items in freq_items}

# Print the dictionary (optional).
print(dict(list(freq_items_to_champion_class.items())[:10]))

file_path = 'freq_items_to_champion_class.pkl'

# Save the dictionary to the file using pickle
with open(file_path, 'wb') as file:
    pickle.dump(freq_items_to_champion_class, file)
