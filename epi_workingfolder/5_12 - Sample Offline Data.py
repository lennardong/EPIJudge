'''
Implement an algorithm that takes an array of distinct elements as input 
returns a subset of the given size of the array elelements. 
All subsets should be equally likely. 
'''

import typing
import random 

def offline_data(customers: typing.List, size: int) -> typing.List: 
    '''
    enumerate till size, swap with random index from i to end of list 
    '''
    len_customer = len(customers)
    for i in range(size - 1): 
        idx_random = random.randint(i, len_customer) #generate a random index 
        customers[i], customers[idx_random] = customers[idx_random], customers[i] #swap 
    
    return customers
        
        
### TEST CASE 
input = [i for i in range(100)]
print (offline_data(input, 20))