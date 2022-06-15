

def test_palin(txt: str) -> bool: 
    '''
    concept: construct a zip, check if similar
    '''
    a = list(zip(\
        map(str.lower,filter(str.isalnum,txt)),
        map(str.lower,filter(str.isalnum,reversed(txt)))
    )) #LEARNING: mehods are not given () in map. why? 

    return all([letter_forward == letter_backward for letter_forward, letter_backward in a])

def test_palinv2 (txt: str) -> bool: 
    '''
    traverse the front and back, comparing them 
    return false and break 
    '''
    idx_front = 0
    idx_back = len(txt) - 1
    
    while idx_front < idx_back: #how do define if they cross? 
        # if not alphanumeric, to move forward 
        while not txt[idx_front].isalnum() and idx_front < idx_back:
            idx_front += 1 
            print (f'...idx_front: {idx_front}, letter: {txt[idx_front]}')
        while not txt[idx_back].isalnum() and idx_front < idx_back:
            idx_back -= 1
            print (f'...idx_back: {idx_back}, letter: {txt[idx_back]}')
        
        #compare
        print (f'idx_front: {txt[idx_front].lower()}, {idx_front} | idx_back: {txt[idx_back].lower()}, {idx_back} \n')
        if txt[idx_front].lower() != txt[idx_back].lower():
            return False
        
        idx_front, idx_back = idx_front + 1, idx_back - 1 
            
    return True
        


## TEST CASES 
a = 'A man, a plan, a canal, panama'
b = 'able was i, ere I saw Elba!'
# print (test_palin(a))
print (test_palinv2(b))