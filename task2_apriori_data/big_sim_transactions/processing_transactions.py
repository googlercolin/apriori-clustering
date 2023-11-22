import pandas as pd
import csv
from apyori import apriori, dump_as_json, load_transactions
from tqdm import tqdm
import numpy as np


# with pd.read_csv('transactions.csv', chunksize=500000, usecols=['CUST_ID', 'DATE', 'EXP_TYPE']) as reader:
#     for idx, chunk in enumerate(reader):
#         if idx < 700:
#             print(f"idx: {idx}")
#             continue
#         else:
#             print("getting new data")
#             df = reader.get_chunk(150000000)
#             print("here")
#             # Sort by two columns 
#             sorted_df = df.sort_values(['CUST_ID', 'DATE'], ascending = [True, True])
#             sorted_df.to_csv('subtransactions4.csv')  
#             break

    # prev: 50000000 (100)
    # prev: 300000000 (600)
    


prev_cust_id = ''
prev_date = ''
current_exp_type = []
# # open('subtransactions.txt', 'w').close()

df = pd.read_csv('subtransactions3.csv')

with open('subtransactions.txt', 'a') as f:

    for index, row in df.iterrows():
        if np.random.choice([0,1]) == 0:
            continue
        if index == 0:
            prev_cust_id = row['CUST_ID']
            prev_date = row['DATE']
            current_exp_type.append(row['EXP_TYPE'])
        if index == len(df):
            f.write(",".join(current_exp_type) + '\n')
            break
        if row['CUST_ID'] == prev_cust_id and row['DATE'] == prev_date:
            current_exp_type.append(row['EXP_TYPE'])
        else:
            f.write(",".join(current_exp_type) + '\n')
            current_exp_type = []
            # Save current diff detail
            prev_cust_id = row['CUST_ID']
            prev_date = row['DATE']
            current_exp_type.append(row['EXP_TYPE'])

