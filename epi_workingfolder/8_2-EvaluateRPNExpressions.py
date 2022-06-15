'''
Output: an integter that the expression evaluates to 
Input: a string

Considerations
String is 'Reverse Polish Notation' (RPN) if 
1) single digit(s) prefixed with an optional - (i.e. a positive or negative integer)
2) it is the form "A, B, C", where A and B are RPN expressions and C is +-*/. 

A RPN can be evaluated uniquely to an integer, which is determined recursively. 
1) Basecase - rule 1
2) Recusive case - rule 2.
3) e.g. 

In practice RPN can be conveniently evaluated using a stack structure. Reading the expression from left to right, the following operations are performed:

1. If a value appears next in the expression, push this value on to the stack.
2. If an operator appears next, pop two items from the top of the stack and push the result of the operation on to the stack.

Examples
"2, 3, X" evaluates to 6 
"3, 4, +, 2, X, 1, +" = (3 + 4) * 2 + 1 = 15
'''

def evaluate_rpn(expr: str) -> int: 
    # Concept: Stack Extraction: create a stack and pop out previous two numbers based on expression hits. 
    # 1. create a lookup for operands and lambda for execution 
    # 2. convert to list, splitting at delimiter (,)
    # 3. iterate through till finding the operands. backtrack two steps and perform the operand on it. when done, cycle from start again. 

    cache = []
    DELIM = ','
    OPER_LOOKUP = {
        '+': lambda a, b: a + b, 
        '-': lambda a, b: a - b,
        'X': lambda a, b: a * b, 
        '/': lambda a, b: int(a / b)
    }

    for item in expr.split(DELIM):
        if item in OPER_LOOKUP: 
            cache.append(OPER_LOOKUP[item](cache.pop(), cache.pop()))
        else: 
            cache.append(int(item))
    return cache[0]

### TEST CASES
a = '3, 4,+,2,X,1,+'
print (evaluate_rpn(a))


### LEARNING QUESTIONS 

'''
Q: what does int(   2   ) evalute to? 
A: 2. the spaces are automatically stripped. 

Q: give an example of a dictionary lookup
A: in a Reverse Polish notation, a dicionary lookup for Operands can be used to evalute the previous two integers in a stack

'''