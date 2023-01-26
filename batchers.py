from random import randrange 
##for small db
# DAILY_BATCHES = 6
# MAX_BATCH_SIZE = 2

# # for large db
DAILY_BATCHES = 40
MAX_BATCH_SIZE = 6

def rearrangeResults(results): 
    """
    Rearrange array such that no two adjacent elements are next to each other.
    """
    for i in range(len(results) -1): 
        while results[i] == results[i+1]: 
            j = randrange(len(results)) 
            results[i], results[j] = results[j], results[i] #swap places 
    return results 

def unique_tuple(tup): 
    """
    Ensure that all elements inside of the batch are unique and match the MAX_BATCH_SIZE req.
    """
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

def match_batch_size(results): 
    """
    Binary Variance of Inserting empty batches and periodically split a batch to match DAILY_BATCHES.
    """
    low = 0  
    high = len(results) 
    while (len(results) != DAILY_BATCHES) or (low <= high): 
        mid = low + (high - low) // 2 
        # add empty spaces in between mid 
        left = results[0: mid]
        right = results[mid +1: len(results)] 
        middle = results[mid] 

        tuple_results = left + [(' ',)] + [middle] + [(' ',)] + right 
        results = tuple_results 
        
        if len(results) == DAILY_BATCHES: 
            return results
        elif len(results) < DAILY_BATCHES: 
            #split each tuple into mini tuple element at a time and check 
            print("HELLO")
            for tup_batch in results: 
                print(tup_batch)
                #this is the first tuple batch 
                pos = results.index(tup_batch)
                results.remove(tup_batch)
                args = tuple(zip(*[iter(tup_batch)]*(MAX_BATCH_SIZE - 1))) 
                print(args)
                for idx, arg in enumerate(args): 
                    results.insert(pos, arg)
                    pos += 1 
                    singles = args[idx + 1: len(args)]
                    rem = tuple()
                    for single in singles: 
                        rem += single 
                    results.insert(pos, rem)
                    pos += 1 
                    if len(results) == DAILY_BATCHES: 
                        return results 
            high = mid - 1 
        else: 
            #remove empty batches 
            results.remove((' ',))
            low = mid + 1 
    return results 
        

def create_batches(updated_product): 
    """
    creates unique pattern for batch matching its frequency. 
    This is how we map the days with batches on db.csv 
    day 1: (A) | (B) | () |  (A, C) | () |(A) 
    day 2: (A) | (B) | () |   (A)   | () |(A) 
    day 3: (A) | (B) | () |   (A)   | () |(A) 
    day 4: (A) | (B) | () |  (A, C) | () |(A) 
    day 5: (A) | (B) | () |   (A)   | () |(A) 
    day 6: (A) | (B) | () |   (A)   | () |(A) 
    day 7: (A) | (B) | () |  (A, C) | () |(A) 
    """
    #update all value type to float 
    for key, val in updated_product.items(): 
        updated_product[key] = float(val)
    tup = tuple()
    #find maximum value from dictionary 
    control_loop = int(float(max(list(updated_product.values())))) 
    while control_loop > 0: 
        for key, val in updated_product.items(): 
            val = float(val)
            if val >0: 
                updated_product[key] = val - 1.0 #decrement  
                tup += (key,) 
        control_loop = int(float(max(list(updated_product.values())))) #need to update dictionary 

    batches = unique_tuple(tup)
    final_batches = rearrangeResults(match_batch_size(batches))
    if len(final_batches) <= 0:
        raise ValueError(
            "Cannot have 0 or negative number of batches. Current number: {}".format(
                len(final_batches)
            )
        )

    return final_batches 



    


