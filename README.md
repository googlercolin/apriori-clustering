# apriori-clustering

This code implements the tasks for Apriori Algorithm + Clustering with Frequent Itemsets.

## Contents
- [Tasks](#tasks)
  - [Task 1](#task-1)
  - [Task 2](#task-2)
  - [Task 3](#task-3)
  - [Task 4](#task-4)  
- [Contributors](#contributors)

## Tasks

### Task 1
To implement the Apriori algorithm, we referenced the following online sources [1], [2], [3] to get inspiration. We then implemented our own version from scratch, incorporating the Fk-1* Fk-1 method for candidate generation and candidate pruning when subsets are infrequent. This helps to significantly reduce memory usage. In addition, support counting is done by opening a .csv file and iterating through each transaction sequentially to count each itemset. This disk-based approach is implemented in the “count_candidate_itemsets” function to ensure that we can read input files that are larger than our memory. We also made use of the `time` and `tqdm` libraries to time our algorithm function and monitor the progress of the program. 

To show that resulting frequent item sets that our code produces are accurate, we have an additional `verify_support` function, that counts the occurrences of the frequent item sets in the original input file and checks that it matches with the resulting count we had in our Apriori algorithm function. In testing the disk-based code implementation, we ran our Apriori algorithm on a large dataset of 4.6GB containing 150M rows of transactions. Using a conservatively larger minimum support of 10M (~6.6%), it ran smoothly and produced 9 frequent itemsets.

[1] 	“Apriori-and-Eclat-Frequent-Itemset-Mining/apriori.py at master · andi611/Apriori-and-Eclat-Frequent-Itemset-Mining,” GitHub, 2023. https://github.com/andi611/Apriori-and-Eclat-Frequent-Itemset-Mining/blob/master/apriori.py (accessed Nov. 02, 2023).

[2] 	“Data-Mining-Algorithms/apriori.py at master · ganit44/Data-Mining-Algorithms,” GitHub, 2023. https://github.com/ganit44/Data-Mining-Algorithms/blob/master/apriori.py (accessed Nov. 02, 2023).

[3] 	“Apriori-Algorithm/AprioriAlgorithm.py at master · MrPatel95/Apriori-Algorithm,” GitHub, 2023. https://github.com/MrPatel95/Apriori-Algorithm/blob/master/AprioriAlgorithm.py (accessed Nov. 02, 2023).


### Task 2 
Runs Apriori algorithm from Task 1 on 3 datasets with different minimum support thresholds. Datasets used:
- [League of Legends Ranked Matches](https://www.kaggle.com/datasets/paololol/league-of-legends-ranked-matches/data)
- [Instacart Market Basket Analysis](https://www.kaggle.com/competitions/instacart-market-basket-analysis/data)
- [Simulated Retail Transactions of 75,000 Customers](https://www.kaggle.com/datasets/conorsully1/simulated-transactions)

Reports execution time, number of frequent itemsets, and maximum frequent itemset size for each run.

### Task 3
Uses frequent itemsets as features for clustering using DBSCAN and K-Means clustering. Evaluates clustering effectiveness on 2 labeled datasets.

### Task 4
Implements algorithm to improve performance of Task 3 methods. Provides code for GridSearch and Normalization approaches. Evaluates improved algorithm on same datasets.

## Contributors

- Hong Fung Heng, Colin
- Marcus Tan Song Huang
- Rhys Lie
- Tong Min, Grace