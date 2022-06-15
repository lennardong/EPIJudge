'''
generate an entry of the sequence from the previous entry
read off the digits of the previous entry, counting the number of digits in groups of the same digit

input: n, integer
return: nth integer of n in sequence
'''
def look_and_say(n: int) -> list: 

    def count_string(s: str) -> str: 
        res = ''
        count = 1 
        idx = 0 
        s += '-'
        while idx < len(s) - 1: 
            #print (f'DEBUG... idx: {idx}')
            if s[idx] != s[idx + 1]: # if next number is not the same, write it to the result 
                res += str(count)
                res += s[idx]
                count = 1
                idx += 1 
                print (f'DEBUG...num_run ({s[idx]}) ended: {res}')
            else:  #if next number is the same, increase the count 
                count += 1
                idx += 1 
                #print (f'num_run ongoing...')
        return res 
    
    round = 1
    input = str(n)
    while round != n: 
        print (f'\nROUND: {round} | INPUT: {input}')
        input = count_string(input)
        round += 1 

    return input 


print(look_and_say(6))


### TEST CASES 

n = 3 
n_ans = [3, 13, 1113]

n2 = 5
n_ans = [5, 15, 1115, 3115, 132115, 1115122115]
