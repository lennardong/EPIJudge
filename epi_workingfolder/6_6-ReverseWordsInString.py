
# Reverse all words in a strong. 
# skip whitespace, include punctuation

import string

def reverse_string(s: str) -> str: 
    
    # concept: 
    # 1) loop 1: find all whitespace locations
    # 2) use that to break words up
    
    whitespace = []
    for idx,letter in enumerate(s): 
        if letter == ' ':
            whitespace.append(idx)
    print (whitespace)

    word_start = 0
    while whitespace:
        space = whitespace.pop(0)
        s = s[space:] + ' ' + s[word_start:space]
        word_start = space
        print (f'whitespace: {whitespace}, sentence: {s}')
    return (s)

def reverse_stringv2(s: str) -> str: 

    # challenge: do this in space O(1)
    # concept: 
    # 1) convert string to list using split.
    # 2) reconstruct string with list reversal 
    
    s = s.strip(string.punctuation)
    return ' '.join(list(reversed(s.split(' '))))

def reverse_stringv3 (s: str) -> str: 
    '''
    # CHALLENGE: uses fundamental list operations 
    '''
    
    s = list(s)

    def reversal(start:int, end: int, s: list) -> list:
        
        # Reverse a list based on the start and end index
        
        while start < end:
            s[start], s[end] = s[end], s[start]
            start, end = start + 1, end - 1 
    
    # Revese the whole string 

    reversal(0, len(s)-1, s)
    print ('DEBUG, whole string reversal: ', ''.join(s))
    
    # Reverse each word 
    # 1. use a while True for inifinite loop
    # 2. use a idx_start and idx_end for each work 
    # 3. define idx_end by start of a space
    
    idx_start = 0 
    trigger = True 
    while trigger: 
        idx_end = idx_start
        
        while idx_end < len(s) and s[idx_end] != ' ': #learning: when using while, its better to use < rather than == 
            idx_end += 1 
            trigger = False if idx_end == len(s) else True 
        
        reversal(idx_start, idx_end - 1, s) # reverse 
        print ('DEBUG, word reversal:', ''.join(s[idx_start:idx_end + 1]))
        idx_start = idx_end + 1 # resest idx_start 
    #reversal(idx_start, idx_end, s)
    return ''.join(s)

### TEST CASE 
a = 'Bob likes Alice'
b = 'Bob likes Alice.'
print (reverse_stringv2(a))
print (reverse_stringv2(b))
print (reverse_stringv3(a))
print (reverse_stringv3(b))