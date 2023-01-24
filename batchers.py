from email import header
from typing import List, Dict
from math import ceil
import datetime
import random
import csv 

# for small db
DAILY_BATCHES = 6
MAX_BATCH_SIZE = 2

#Read csv file 
datafile = "db.csv"
product_frequency = {} 
with open(datafile, mode="r") as inp: 
    reader = csv.reader(inp) 
    product_frequency = {rows[0]: rows[1] for rows in reader[1:]} 

# # for large db
# DAILY_BATCHES = 40
# MAX_BATCH_SIZE = 6

# def create_batches(
#     # Your list of args
# ) -> List[str]:
#     """
#     Create a required number of scraping batches. Presumed this will be run once daily

#     :param num_batches: Total number of batches to create. Assumed to be a daily value
#     :param max_batch_size: Maximum size of each batch. actual size <= max_batch_size
#     :Add more params as you may require:
#     :raises ValueError: if the defined num_batches <= 0 or max_batch_size < 1
#     """
#     if num_batches <= 0:
#         raise ValueError(
#             "Cannot have 0 or negative number of batches. Current number: {}".format(
#                 num_batches
#             )
#         )
#     if max_batch_size < 1:
#         raise ValueError(
#             "Cannot have 0 or negative maximum batch size. Current number: {}".format(
#                 max_batch_size
#             )
#         )
    

#     # You will need to fake moving time forward. You are free to decide
#     # How small/big each time step will be
#     time_step = # 
#     batches = []
#     for i in range(num_batches):
#         batch = create_batch()  # create_batch will need some args
#         batches.append(batch)
#         current_datetime += time_step
#         create_batch_kwarg["current_datetime"] = current_datetime 
#     return batches
    


# def create_batch(
#     # You may include whichever args you need
# ) -> str:

#     # Your code here ...
#     return batch

# def create_batches(
#     # Your list of args
# ) -> List[str]:
#     """
#     Create a required number of scraping batches. Presumed this will be run once daily

#     :param num_batches: Total number of batches to create. Assumed to be a daily value
#     :param max_batch_size: Maximum size of each batch. actual size <= max_batch_size
#     :Add more params as you may require:
#     :raises ValueError: if the defined num_batches <= 0 or max_batch_size < 1
#     """
#     if num_batches <= 0:
#         raise ValueError(
#             "Cannot have 0 or negative number of batches. Current number: {}".format(
#                 num_batches
#             )
#         )
#     if max_batch_size < 1:
#         raise ValueError(
#             "Cannot have 0 or negative maximum batch size. Current number: {}".format(
#                 max_batch_size
#             )
#         )
    

#     # You will need to fake moving time forward. You are free to decide
#     # How small/big each time step will be
#     time_step = #
#     batches = []
#     for i in range(num_batches):
#         batch = create_batch()  # create_batch will need some args
#         batches.append(batch)
#         current_datetime += time_step
#         create_batch_kwarg["current_datetime"] = current_datetime 
#     return batches
    


# def create_batch(
#     # You may include whichever args you need
# ) -> str:

#     # Your code here ...
#     return batch

def create_batch_content(): 
    for key, val in product_frequency.items(): 
        res = tuple()
        if val > 0:  
            res.append(key)
            product_frequency[key] -= val 


def create_batches() -> List[str]:
    """
    This is how we map the days with batches on db.csv 
    day 1: (A, B) | (A, C) | (A) 
    day 2: (A, B) | (A)    | (A) 
    day 3: (A, B) | (A)    | (A)
    day 4: (A, B) | (A, C) | (A) 
    day 5: (A, B) | (A)    | (A) 
    day 6: (A, B) | (A)    | (A)
    day 7: (A, B) | (A, C) | (A)
    """

    if MAX_BATCH_SIZE <1: 
        raise ValueError(
             "Cannot have 0 or negative maximum batch size. Current number: {}".format(
              MAX_BATCH_SIZE
            )
        ) 

    num_batches = 0 
    while num_batches < DAILY_BATCHES: 
        #create content for our batch 

        num_batches +=1 
    


