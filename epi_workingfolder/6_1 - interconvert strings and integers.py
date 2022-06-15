'''
take a string representing an integre and return the corresponding integer
and vice versa

- code should handle negative integers
- code should handle a leading '+'
- cannot use library functions like int
'''
import functools
import string

def string_to_intv2(s: str) -> int: 
    '''
    uses piecemeal code, 
    1. create an accumulator, which here is an integer
    2. stepthrough the string and convert to int using idx == number trick 
    3. add to accumulator, expand accumuator by * 10 
    
    edges: 
    - account for +- in it 
    - account for negative 
    '''
    res = 0 
    mult = -1 if s[0] == '-' else 1 
    for val in s.strip('-+'):
        res *= 10 
        res += string.digits.find(val)
    return res * mult 

def string_to_int(s: str) -> int: 
    '''
    guided example. uses reduce and preseeds it with an integer. 
    '''
    return (-1 if s[0] == '-' else 1) * functools.reduce(
        lambda running_sum, c: running_sum * 10 + string.digits.find(c),
        s.strip('-+'), 0)

## TEST CASES 

print (string_to_int('+5656'))
print (string_to_int('-5656'))
print (string_to_intv2('+5656'))
print (string_to_intv2('-5656'))

##
def int_to_string(num: int) -> str: 
    '''
    1. go through the int back to front, convert to digit
    2. append it to list 
    3. add - or + as needed 
    4. reverse the list and join it 

    considerations
    - check for negative sign
    '''
    res = ''
    neg = True if num < 0 else False 
    num = num * -1 if num < 0 else num

    while num: 
        res += string.digits[num % 10]
        num //= 10 
    
    return res[::-1] if not neg else (res + '-')[::-1]

## TEST CASES 
print(int_to_string(123))
print(int_to_string(-123))
print(int_to_string(+123))

