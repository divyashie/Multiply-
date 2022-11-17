from typing import List, Dict
from math import ceil
import datetime
import random

def create_batches(
    # Your list of args
) -> List[str]:
    """
    Create a required number of scraping batches. Presumed this will be run once daily

    :param num_batches: Total number of batches to create. Assumed to be a daily value
    :param max_batch_size: Maximum size of each batch. actual size <= max_batch_size
    :Add more params as you may require:
    :raises ValueError: if the defined num_batches <= 0 or max_batch_size < 1
    """
    if num_batches <= 0:
        raise ValueError(
            "Cannot have 0 or negative number of batches. Current number: {}".format(
                num_batches
            )
        )
    if max_batch_size < 1:
        raise ValueError(
            "Cannot have 0 or negative maximum batch size. Current number: {}".format(
                max_batch_size
            )
        )
    

    # You will need to fake moving time forward. You are free to decide
    # How small/big each time step will be
    time_step = # XXX
    batches = []
    for i in range(num_batches):
        batch = create_batch()  # create_batch will need some args
        batches.append(batch)
        current_datetime += time_step
        create_batch_kwarg["current_datetime"] = current_datetime 
    return batches
    


def create_batch(
    # You may include whichever args you need
) -> str:

    # Your code here ...
    return batch

