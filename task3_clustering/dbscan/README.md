## DBSCAN Overview

This DBSCAN component comprises several Python scripts for data processing and clustering. The scripts are designed to work with specific input files and perform various tasks, including creating mappings, associating items with classes, and applying clustering algorithms. Below is a brief description of each script:

### 1. `mapper.py`

- **Purpose**: Reads a text file containing numbers, creates a mapping from unique numbers to incrementing indices, and saves the mapping to a pickle file.

- **Input**:
  - Text file path: `soloItems.txt`

- **Output**:
  - Pickle file: `index_to_itemID.pkl`

### 2. `freq_itemsets_to_champion_class.py`

- **Purpose**: Reads two text files, `leagueItemsets.txt` and `item_class.txt`, associates items with champion classes, and saves the mapping to a pickle file.

- **Input**:
  - Text file paths: `leagueItemsets.txt`, `item_class.txt`

- **Output**:
  - Pickle file: `freq_items_to_champion_class.pkl`

### 3. `freq_itemsets_to_depts.py`

- **Purpose**: Reads two text files, `instacartItemsets.txt` and `products.csv`, associates product IDs with department IDs, and saves the mapping to a pickle file.

- **Input**:
  - Text file paths: `instacartItemsets.txt`, `products.csv`

- **Output**:
  - Pickle file: `freq_items_to_depts.pkl`

### 4. `dbscan.py`

- **Purpose**: Reads item entries from a text file, performs DBSCAN clustering on one-hot vectors, associates clusters with item classes, and evaluates clustering accuracy.

- **Input**:
  - Text file path: `leagueItemsets.txt`
  - Pickle file path: `index_to_itemID.pkl`
  - JSON file path: `item_class.txt`

- **Output**:
  - Clustering results and evaluation metrics.

## Running the Scripts

1. Ensure you have Python installed on your system.
2. In your Python environment, install the required Python libraries using: `pip install numpy scikit-learn`
3. Execute each script separately, ensuring the required input files are in the same directory.

## Notes

- Make sure to adjust file paths and filenames as needed.
- Uncomment or modify the print statements for additional information during script execution.
- Review the script outputs for results and metrics.