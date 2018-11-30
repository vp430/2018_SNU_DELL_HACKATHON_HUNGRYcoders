# Apriori

# Importing the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import json

# Data Preprocessing
dataset = pd.read_csv('dellapr.csv', header = None)
transactions = []
for i in range(0, 7501):
    transactions.append([str(dataset.values[i,j]) for j in range(0, 19)])

# Training Apriori on the dataset
from apyori import apriori
rules = apriori(transactions, min_support = 0.003, min_confidence = 0.2, min_lift = 3, min_length = 2)

# Visualising the results
results = list(rules)

results_list = []
results_list1 = list()
for i in range(0, len(results)):
    results_list.append('RULE:\t' + str(results[i][0]) + 
                            '\nSUPPORT:\t' + str(results[i][1]) +
                            '\nCONF:\t' + str(results[i][2][0][2]) +
                            '\nLIFT:\t' + str(results[i][2][0][3]))
    rs = []
    rs.append(str(results[i][0]))
    rs.append(str(results[i][1]))
    rs.append(str(results[i][2][0][2]))
    results_list1.append(rs)
    

results[1][1]

print(json.dumps(results_list1))
pd.DataFrame(results_list1).to_excel('C:\\Users\\Royale121\\Desktop\\apyori.xlsx', header=False, index=False)