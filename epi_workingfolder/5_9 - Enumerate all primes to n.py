import typing

def enumerate_primesv1(num: int) -> typing.List[int]: 
    '''
    Write a program that takes an integer argument and returns all primes between 1 and the integer. 
    e.g. if input is 18, it should return 2, 3, 5, 7, 11, 13, 17 
    
    1. create a is_prime
    2. pre-initialize it with known prime: 1
    3. if number not in is_prime(false), then find all multiples till n
    
    '''
    res = [] 
    is_prime = [True, True] + [False for i in range(2, num + 1)]

    for n in range(2, num + 1):
        if not is_prime[n]: #if in is_prime, skip 
            res.append(n)
            for i in range(n, num+1, n):
                is_prime[i] = True
    return res 

def enumerate_primesv2(num: int) -> typing.List[int]: 
    '''
    construct a dictionary to sieve the thing. 
    '''

    is_prime = {i:False for i in range(1, num+1)}
    is_prime[1] = 'Prime' 

    for n in sorted(is_prime.keys()): 
        if not is_prime[n]: #if true
            is_prime[n] = 'Prime'
            for i in range(n * 2, num + 1, n):
                is_prime[i] = 'Multiple' 
    print (is_prime)

    res = {} #transpose the dictionary
    for k, v in is_prime.items(): 
        if res.get(v) == None: 
            res[v] = [k]
        else: 
            res[v].append(k)
    
    print (res)

    return res['Prime']


### TEST CASES 
n = 19
n_result = [2,3,5,7,11,13,17,19]

print(enumerate_primesv1(n))
print(enumerate_primesv2(n))



# are keys kept ordered? 