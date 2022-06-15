'''
Output: boolean True/False 
Input: a string 

Considerations:
- a well-formed string is defined as one where each open has a closed. (), [], {} 
- characters: ({[]})

Examples: 
TRUE 
([[[{[]}]]]())
{}[]{{()}[]}

FALSE 
([[{[]}]]]())
{}]{{()}[]}

'''
def test_string_for_wellformedness(expr: str) -> bool: 
    '''
    Concept: 
    - it is false if there is 1) a stray right or 2) a leftover left
    - interate through the expression, store every left into a cache.
    '''
    right_closers = [] 
    LEFT_LOOKUP = {
        '(': ')',
        '{': '}',
        '[': ']',
    }
    RIGHT_LOOKUP = {b: a for a, b in LEFT_LOOKUP.items()}

    for char in expr: 
        #defensive programming: check for valid characters first 
        if char not in LEFT_LOOKUP and char not in RIGHT_LOOKUP:
            continue 
        #check for left 
        elif char in LEFT_LOOKUP:
            right_closers.append(LEFT_LOOKUP.get(char))
        #check for right closer. its implied its not a left closer.
        elif char in right_closers:
            right_closers.remove(char)
        #check for stray. 
        elif char not in right_closers:
            return False 
    
    #check if any leftover left, implied by right closers
    return len(right_closers) == 0 
    


### TEST 
a = ['([[[{[]}]]]())', '([[[{([}]]]]))', '([[{[]}]]]())', '{\}]{\{()}[]}']
for expr in a:
    print (expr, test_string_for_wellformedness(expr))

### SELF QUIZ 

'''
Q: how do you pivot a dictionary using list comprehension? 

Q: how do you pivot a dictionary using zip and lambdas? 

'''