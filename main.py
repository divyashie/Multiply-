"""
Multiply developer skill assessment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
This file and other files within this repository are used for a developer skill
assessment by Multiply (multiply.cloud).

If you have been asked to attempt this assessment, you are free to modify 
any of the files or even create new files if necessary in order to get the 
outcome required in this task.
"""

import csv 
from batchers import * 
import json 

datafile = "db_large.csv"
#datafile = "db.csv"
num_days = 7

def readFile(datafile): 
    product_frequency = {} 
    with open(datafile, mode="r") as inp: 
        reader = csv.reader(inp) 
        product_frequency = {rows[0]: rows[1] for rows in reader}
    del product_frequency['Product'] #removing header 
    return product_frequency

def trackDecimalProduct(product_frequency): 
    tracking_decimal_product = {} 
    for key, val in product_frequency.items(): 
        val = float(val)
        if int(val) % 10 == 0:  #check if its a decimal 
            #track that product and its frequency 
            if val == 0.0:  #handling zero division 
                tracking_decimal_product[key] = 0.0 
            else: 
                tracking_decimal_product[key] = float(round(1/val)) #number of times needs to appear 
    return tracking_decimal_product  
    
def updateProductFrequency(day, product_frequency, decimal_product):
    for key, val in decimal_product.items(): 
        if int(val) == 0: 
            product_frequency[key] = 0.0 #set product frequency to 0.0 for this product 
        else: 
            if day % int(val) == 0: #that's where this product needs to reappear in the product_frequency 
                product_frequency[key] = 1.0 #set product frequency to 1.0 for this product 
            else: 
                product_frequency[key] = 0.0 #set product frequency to 0.0 for this product 
    return product_frequency

def getBatches(): 
    output_file = datafile.split('.')[0] + '.txt'
    for i in range(num_days): 
        product_frequency = readFile(datafile) 
        decimal_product = trackDecimalProduct(product_frequency)
        updated_product_frequency = updateProductFrequency(i, product_frequency, decimal_product)
        list_batches = create_batches(updated_product_frequency)
        day = f"{i + 1}" 
        data_dict = {"day ": day}
        for idx, batch in enumerate(list_batches): 
            data_dict.update({f"batch {idx+1}" : batch})

        with open(output_file, 'a') as output: 
            output.write(json.dumps(data_dict))
            output.write('\n')

    return list_batches 

def main(): 
    getBatches()

if __name__ == "__main__":
    main()



