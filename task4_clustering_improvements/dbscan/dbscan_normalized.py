import pickle
import numpy as np
from sklearn.cluster import DBSCAN
from sklearn.metrics.cluster import v_measure_score
from collections import Counter

# Load the mapping from the pickle file
input_mapping_file_path = 'index_to_itemID.pkl'
with open(input_mapping_file_path, 'rb') as pickle_file:
    index_to_itemID = pickle.load(pickle_file)

# Specify the path to your text file containing entries
input_entries_file_path = 'instacartItemsets.txt'

# Read entries from the text file
with open(input_entries_file_path, 'r') as file:
    entries = [list(map(int, line.strip().split(','))) for line in file]

# Create one-hot vectors for each entry
one_hot_vectors = []
for entry in entries:
    one_hot_vector = np.zeros(len(index_to_itemID), dtype=int)
    for item_id in entry:
        if item_id in index_to_itemID.values():
            index = [idx for idx, id in index_to_itemID.items() if id == item_id][0]
            one_hot_vector[index] = 1
    one_hot_vectors.append(one_hot_vector)

# Perform DBSCAN clustering on the one-hot vectors
eps = 0.0025  # epsilon, the maximum distance between two samples for one to be considered as in the neighborhood of the other
min_samples = 2  # minimum number of samples in a neighborhood for a point to be considered a core point
dbscan = DBSCAN(eps=eps, min_samples=min_samples, metric='hamming', n_jobs=-1)
labels = dbscan.fit_predict(one_hot_vectors)

# Create a dictionary to store items for each cluster
cluster_items = {}
for label, entry in zip(labels, entries):
    if label not in cluster_items:
        cluster_items[label] = []
    cluster_items[label].append(entry)

# Load the item to department mapping from the products.csv file
item_department_mapping = {}
with open('products.csv', 'r') as file:
    next(file)  # Skip the header
    for line in file:
        parts = line.strip().split(',')
        item_id, department_id = int(parts[0]), int(parts[-1])
        item_department_mapping[item_id] = department_id

# Create a dictionary to store the itemsets mapped to department IDs
itemset_department_mapping = {}

# Calculate the total count for each department across all clusters
department_total_count = Counter()
for cluster_id, item_arrays in cluster_items.items():
    department_count = Counter()

    for item_array in item_arrays:
        itemset = tuple(item_array)  # Convert the item array to a tuple
        for item_id in itemset:
            if item_id in item_department_mapping:
                department_id = item_department_mapping[item_id]
                department_count[department_id] += 1
                department_total_count[department_id] += 1

    # Normalize department_count over the total items in each department
    for department_id in department_count:
        department_count[department_id] /= department_total_count[department_id]

    # Calculate the majority department for each cluster, considering normalized counts
    majority_department = max(department_count, key=department_count.get)

    # Store the itemset mapped to the majority department in the dictionary
    itemset_department_mapping[itemset] = majority_department

file_path = 'freq_items_to_depts.pkl'
# Open pickle
with open(file_path, 'rb') as file:
    true_labels = pickle.load(file)

# Calculate accuracy
correct_predictions = 0
total_predictions = 0

# Lists to store true and predicted labels
true_labels_list = []
predicted_labels_list = []

for itemset, true_department in true_labels.items():
    if itemset in itemset_department_mapping:
        predicted_department = itemset_department_mapping[itemset]
        true_labels_list.append(true_department)
        predicted_labels_list.append(predicted_department)

        if predicted_department == true_department:
            correct_predictions += 1
        total_predictions += 1

accuracy = correct_predictions / total_predictions if total_predictions > 0 else 0

# Calculate V-Measure
v_measure = v_measure_score(true_labels_list, predicted_labels_list)

print(f"Parameters: eps={eps}, min_samples={min_samples}\t|\tAccuracy: {accuracy * 100:.2f}%\t|\tV-Measure: {v_measure:.4f}")

