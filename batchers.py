# for small db
DAILY_BATCHES = 6
MAX_BATCH_SIZE = 2

# # for large db
# DAILY_BATCHES = 40
# MAX_BATCH_SIZE = 6
    
def unique_tuple(tup): 
    #Ensures that MAX_BATCH_SIZE is respected for each batch 
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
    final_results =[]
    #need to strategically add empty batches 
    while len(results) != DAILY_BATCHES: 
        low = 0
        high = len(results) 
        while low <= high: 
            mid = low + (high - low) // 2 
            if mid == 0: 
                break 
            left = results[0: mid][0] 
            right = results[mid+ 1: len(results)][0]
            middle = results[mid]
            
            final_results.append(left)
            final_results.append((' ',))
            final_results.append(middle)
            final_results.append((' ',))
            final_results.append(right)
            results = final_results 
            
            if len(results) == DAILY_BATCHES: 
                return results 
                
            if len(results) < DAILY_BATCHES: 
                #split tuple into 1 each 
                args = tuple(zip(*[iter(left)]*1)) #(A) , (B)
                pos = results.index(left)
                results.remove(left) 
                for arg in args: 
                    results.insert(pos, arg)
                    rem = tuple()
                    for arg in args[1:]: 
                        rem += arg 
                    results.insert(pos+1, rem) #split one item at it to check against if length has increased 
                    #check if len(results) meet required size and break 
                    if len(results) == DAILY_BATCHES: 
                        return results 
                    pos += 1 
                high = mid -1 
            else: 
                #remove empty batches 
                results.remove((' ',))
                low = mid + 1 
        return results
        

def create_batches(updated_product): 
    """
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

    print(tup)
    batches = unique_tuple(tup)
    final_batches = match_batch_size(batches)
    if len(final_batches) <= 0:
        raise ValueError(
            "Cannot have 0 or negative number of batches. Current number: {}".format(
                len(final_batches)
            )
        )

    return final_batches 



    


