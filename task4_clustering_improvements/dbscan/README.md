# DBSCAN Improvements

## 1. `dbscan_gridsearch_v.py`

### Overview

The `dbscan_gridsearch_v.py` script performs a grid search for optimal DBSCAN parameters, clustering item entries based on one-hot vectors. It evaluates clustering quality using V-Measure and accuracy metrics.

### Workflow

1. **Load Mapping:** Load the mapping from the pickle file (`index_to_itemID.pkl`).

2. **Read Entries:** Read item entries from the text file (`instacartItemsets.txt`).

3. **Create One-Hot Vectors:** Convert item entries into one-hot vectors based on the loaded mapping.

4. **Grid Search:** Iterate through a predefined parameter grid and perform DBSCAN clustering. Evaluate each set of parameters using V-Measure and accuracy.

5. **Results:** Print the results for each parameter combination, including V-Measure, accuracy, and parameters.

6. **Best Parameters:** Display the best-performing parameters and their corresponding V-Measure.

## 2. `dbscan_normalized.py`

### Overview

The `dbscan_normalized.py` script applies DBSCAN clustering on one-hot vectors of item entries. It normalizes department counts within clusters, considering the total count of each department across all clusters. The script evaluates clustering quality using V-Measure, accuracy, and prints the results.

### Workflow

1. **Load Mapping:** Load the mapping from the pickle file (`index_to_itemID.pkl`).

2. **Read Entries:** Read item entries from the text file (`instacartItemsets.txt`).

3. **Create One-Hot Vectors:** Convert item entries into one-hot vectors based on the loaded mapping.

4. **DBSCAN Clustering:** Perform DBSCAN clustering with specified parameters.

5. **Department Mapping:** Load the item to department mapping from the CSV file (`products.csv`).

6. **Normalized Counts:** Calculate normalized department counts within each cluster.

7. **Majority Department:** Determine the majority department for each cluster based on normalized counts.

8. **Results:** Print accuracy, V-Measure, and parameters.

## Running the Scripts

To run the scripts:

1. Ensure you have Python installed on your system.
2. Install the required Python libraries using: `pip install numpy scikit-learn`
3. Execute the script.

**Note:** Adjust file paths and filenames as necessary.