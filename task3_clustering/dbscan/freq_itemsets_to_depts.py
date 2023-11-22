import csv
from collections import Counter
import pickle

tx_freq_items = []

# Open the text file for reading.
with open('instacartItemsets.txt', 'r') as file:
    # Iterate through each line in the file.
    for line in file:
        # Split the line by ',' to separate key and items.
        parts = line.strip().split(',')
        
        # The remaining elements are items converted to integers and stored in a list.
        items = [int(float(x)) for x in parts]
        
        # Add the key-value pair to the list.
        tx_freq_items.append(items)

product_department_mapping = {}

# Open the CSV file for reading.
with open('products.csv', 'r') as file:
    reader = csv.DictReader(file)
    
    # Iterate through each row in the CSV.
    for row in reader:
        # Extract the product_id and department_id from each row.
        product_id = int(row['product_id'])
        department_id = int(row['department_id'])
        
        # Map the product_id to its department_id in the dictionary.
        product_department_mapping[product_id] = department_id

# Now, product_department_mapping contains the mapping of product_id to department_id.

def majority_department(departments):
    department_count = Counter(departments)
    most_common = department_count.most_common(1)
    return most_common[0][0] if most_common else departments[0]

# Create a new dictionary with the majority department for each list.
freq_items_to_depts = {tuple(product_ids): majority_department([product_department_mapping[product_id] for product_id in product_ids]) for product_ids in tx_freq_items}

# Print the dictionary (optional).
print(dict(list(freq_items_to_depts.items())[:10]))

file_path = 'freq_items_to_depts.pkl'

# Save the dictionary to the file using pickle
with open(file_path, 'wb') as file:
    pickle.dump(freq_items_to_depts, file)
