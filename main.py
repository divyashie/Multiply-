"""
Multiply developer skill assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file and other files within this repository are used for a developer skill
assessment by Multiply (multiply.cloud).

If you have been asked to attempt this assessment, you are free to modify 
any of the files or even create new files if necessary in order to get the 
outcome required in this task.
"""

import datetime
import csv 
from batchers import * 
import pandas as pd 

# datafile = "db_large.csv"
datafile = "db.csv"
num_days = 7

product_frequency = {} 
with open(datafile, mode="r") as inp: 
    reader = csv.reader(inp) 
    product_frequency = {rows[0]: rows[1] for rows in reader}
del product_frequency['Product'] #removing header 
print(product_frequency) 

results_df = pd.DataFrame()
for i in range(num_days): 
    updated_product_frequency = update_product_frequency(i, product_frequency) 
    list_batches = create_batches(updated_product_frequency)
    curr_datetime = datetime.datetime.now()
    curr_datetime += datetime.timedelta(days=i)
    results_df["Daytime"] =  curr_datetime 
    results_df["batches"] = list_batches 

print(results_df.head()) 
results_df.to_csv('results.csv',header=True)

