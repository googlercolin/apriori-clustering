import pickle

# Specify the path to your text file
input_file_path = 'soloItems.txt'

# Read the numbers from the text file
with open(input_file_path, 'r') as file:
    numbers = [int(line.strip()) for line in file]

# Create a mapping from each unique number to an incrementing index
unique_numbers = sorted(set(numbers))
index_to_itemID = {idx: id for idx, id in enumerate(unique_numbers)}

# Save the mapping to a pickle file
output_file_path = 'index_to_itemID.pkl'
with open(output_file_path, 'wb') as pickle_file:
    pickle.dump(index_to_itemID, pickle_file)

# Print the mapping
# print("Number to Index Mapping:")
# for idx, id in index_to_itemID.items():
#     print(f"{idx}: {id}")