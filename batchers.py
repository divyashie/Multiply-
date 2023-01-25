from typing import List, Dict

# for small db
DAILY_BATCHES = 6
MAX_BATCH_SIZE = 2

# # for large db
# DAILY_BATCHES = 40
# MAX_BATCH_SIZE = 6
    
def unique_tuple(tup): 
    res = tuple() 
    results = [] 
    for elem in tup: 
        if elem not in res and len(res) != MAX_BATCH_SIZE: 
            res += (elem,) 
        else: 
            results.append(res)
            res = tuple() 
            res += (elem,) 
    results.append(res)
    return results

def update_product_frequency(day, product_frequency) -> Dict[str, int]: 
    tracking_decimal_product = {} 
    for key, val in product_frequency.items(): 
        if val % 1 != 0:  #check if its a decimal 
            #track that product and its frequency 
            tracking_decimal_product[key] = round(1/val) #number of times needs to appear 
            

    for key, val in tracking_decimal_product.items(): 
        if day % val == 0: #that's where this product needs to reappear in the product_frequency 
            product_frequency[key] = int(1.0) #set product frequency to 1.0 for this product 
        else: 
            product_frequency[key] = int(0.0) #set product frequency to 0.0 for this product 
    return product_frequency
    

def create_batches(updated_product) -> List[str]: 
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
    tup = tuple()
    #find maximum value from dictionary 
    control_loop = int(max(list(updated_product.values()))) 
    while control_loop > 0: 
        for key, val in updated_product.items(): 
            val = int(val)
            if val >0: 
                updated_product[key] = val - 1#decrement  
                tup += (key,) 
        control_loop = int(max(list(updated_product.values()))) #need to update dictionary 

    batches = unique_tuple(tup)
    if len(batches) <= 0:
        raise ValueError(
            "Cannot have 0 or negative number of batches. Current number: {}".format(
                len(batches)
            )
        )

    return batches 



    


