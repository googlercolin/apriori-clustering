import itertools
import time
from collections import defaultdict
from tqdm import tqdm
import sys

def f_method_candidate_generation(frequent_itemsets, k):
    # Currently have a k-1 size frequent itemset
    # Find matching k-2 frequent itemsets
    candidate_itemsets = []
    if k-1 > 1:
        count_dict = defaultdict(int)
        value_dict = defaultdict(list)
        for combi in frequent_itemsets: 
            front_k_items = combi[:k-2]
            count_dict[front_k_items] += 1
            value_dict[front_k_items].append(combi[-1])
        # Check for count >= 2
        match_dict = {k:v for (k, v) in count_dict.items() if v >= 2}
        match_keys = match_dict.keys()
        # Generate candidate sets
        for key in match_keys:
            for ending_combi in itertools.combinations(value_dict[key], 2):
                candidate_itemsets.append(key+ending_combi)
    else:
        # k = 2
        # Generate all 2-itemsets
        candidate_itemsets = list(itertools.combinations(frequent_itemsets, 2))

    return candidate_itemsets

def f_method_candidate_pruning(candidate_itemsets, infrequent_itemsets, k):
    pruned_set = set()
    for candidate in candidate_itemsets:
        subsets = list(itertools.combinations(candidate, k-1))
        # Deal with tuples being generated if combinations is made of just 1 element
        if k == 2:
            subsets = [x[0] for x in subsets]
        for subset in subsets:
            if subset in infrequent_itemsets:
                print(f"Pruning candidate: {candidate} since subset: {subset} is infrequent")
                pruned_set.add(candidate)
                break
    # Remove pruned candidates
    return list(set(candidate_itemsets) - pruned_set)

def count_candidate_itemsets(candidate_itemsets, candidate_count, fileName):
    # Read transactions in disk
    print("Opening file to read from disk...")
    with open(fileName, 'r') as f:
        # Scan through all transactions one by one
        for transaction in tqdm(f):
            items = transaction.strip().split(',')
            # Count occurence of each generated itemset
            for itemset in candidate_itemsets:
                # 2-itemsets and above
                if(set(itemset).issubset(set(items))):
                    candidate_count[itemset] += 1

        for itemset in candidate_itemsets:
            print(f"Itemset: {itemset} | Count: {candidate_count[itemset]}")
    
    print("Finished counting. Closing file...")
    return candidate_count

def count_initial_candidates(candidate_count, fileName):
    # Read transactions in disk
    with open(fileName, 'r') as f:
        for transaction in f:
            # Track occurence count of each item in all transactions
            for item in set(transaction.strip().split(',')):
                candidate_count[item] += 1
    
    return candidate_count

def apriori(candidate_count, minsup):
    frequent_itemsets = set()
    infrequent_itemsets = set()
    result_frequent_itemsets = set()

    print('======= Candidate Sets 1 (C1) =======')
    candidate_count = count_initial_candidates(candidate_count, fileName)
    for item in candidate_count:
        print(f"Itemset: ({item}) | Count: {candidate_count[item]}")
            
    print('======= Frequent Itemsets 1 (F1) =======')
    for item in candidate_count:
        if(candidate_count[item] >= minsup):
            print(f"Frequent Itemset: ({item}) | Count: {candidate_count[item]}")
            frequent_itemsets.add(item)
        else:
            infrequent_itemsets.add(item)

    if len(frequent_itemsets) == 0:
        print("No Frequent Itemsets Found")
        raise

    result_frequent_itemsets.update(frequent_itemsets)

    print("\n\n")
    # Start iteration from k = 2 size of itemset
    k = 2

    while(len(frequent_itemsets) > 1):
        # Brute Force method
        # candidate_itemsets = list(itertools.combinations(unique_items, k))

        # F_k-1 * F_k-1 method
        # For each combination of F_k-1, check if their first k-1 items are identical
        candidate_itemsets = f_method_candidate_generation(frequent_itemsets, k)
        print(f"After Generation: {candidate_itemsets}")
        print(f"Size of Candidate Itemsets: {len(candidate_itemsets)}")
        # Iterate through each candidate and check if their subsets of length k-1 are infrequent
        candidate_itemsets = f_method_candidate_pruning(candidate_itemsets, infrequent_itemsets, k)
        print(f"After Pruning: {candidate_itemsets}")
        print(f"Size of Candidate Itemsets: {len(candidate_itemsets)}")

        unique_frequent_items = set()
        frequent_itemsets = set()
        infrequent_itemsets = set()

        # Support counting
        print(f'======= Candidate Sets {k} (C{k}) =======')
        candidate_count = count_candidate_itemsets(candidate_itemsets, candidate_count, fileName)
            
        print(f'======= Frequent Itemsets {k} (F{k}) =======')
        for itemset in candidate_itemsets:
            if candidate_count[itemset] >= minsup:
                print(f"Frequent Itemset: {itemset} | Count: {candidate_count[itemset]}")
                frequent_itemsets.add(itemset)
                for item in itemset:
                    unique_frequent_items.add(item)
            else:
                infrequent_itemsets.add(itemset)

        result_frequent_itemsets.update(frequent_itemsets)            
        print("\n\n")
        k += 1

    return list(result_frequent_itemsets), candidate_count

def verify_support(frequent_itemsets, apriori_counts, fileName):
    # Verify count of each determined frequent_itemset and match it with our apriori algorithm count
    verified_counts = defaultdict(int)
    with open(fileName, 'r') as f:
        # Check all transactions
        for transaction in f:
            items = transaction.strip().split(',')
            # Count occurence of frequent itemset to verify 
            for itemset in frequent_itemsets:
                # Deal with 1-itemset being a string
                if isinstance(itemset, str):
                    if({itemset}).issubset(set(items)):
                        verified_counts[itemset] += 1
                else:
                    if(set(itemset).issubset(set(items))):
                        verified_counts[itemset] += 1

    # Compare counts with our apriori resulting counts
    max_frequent_itemset_size = 0
    for itemset in frequent_itemsets:
        if isinstance(itemset, str):
            max_frequent_itemset_size = max(max_frequent_itemset_size, 1)
        else:
            max_frequent_itemset_size = max(max_frequent_itemset_size, len(itemset))
        if verified_counts[itemset] != apriori_counts[itemset]:
            print(f"Mismatch in counts found for itemset {itemset}!")
            print(f"verified_counts: {verified_counts[itemset]}, apriori_counts: {apriori_counts[itemset]}")
    
    print("Verification Complete!")
    print(f"Max Frequent Itemset Size: {max_frequent_itemset_size}")

if __name__ == "__main__": 
    # Writing console outputs to txt
    sys.stdout = open('result.txt', 'w')
    # Reading Input 
    fileName = "candies.txt"
    # Minsup as percentage of database set. Manually change the number of transactions.
    minsup = int(0.3 * 25)
    # minsup = 10000000

    print(f"Initializing Apriori algorithm with minsup: {minsup}")
    start = time.time()
    frequent_itemsets, apriori_counts = apriori(defaultdict(int), minsup)
    end = time.time()
    print(f"Algorithm running time: {end - start} seconds")
    # Verify support of frequent itemset by checking through transactions manually again
    verify_support(frequent_itemsets, apriori_counts, fileName)

    print(f"There are {len(frequent_itemsets)} Frequent Itemsets: \n", frequent_itemsets)

    sys.stdout.close()

