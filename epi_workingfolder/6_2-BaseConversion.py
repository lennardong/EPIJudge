'''
Write a program that performs base conversion 
The input is a string, an integer b1 and another integer b2
The output should be the string representing the integer in base b2. 

Notes 
- Assume 2 <= b1, B2 <= 16
- Use A to represent 10, B for 11, ... and F for 15. 

Example 
Inputs: 
- string '615'
- b1 = 7
- b2 = 13
Result: 
1A7 >>> 6 * 7**2 + 1 * 7  + 5 = 1 * 13 ** 2 + 10 * 13 + 7 
'''

def base_conversion(str_num: str, b1: int, b2: int) -> str: 
    '''
    concept: 
    1. convert b1 to base10 by going in reverse
    2. convert base10 to b2 
    '''
    base10, pow, res = 0, 0, ''
    neg = False 
    conversion = {
        10:'A',
        11:'B',
        12:'C',
        13:'D',
        14:'E',
        15:'F', 
    }

    #convert b1 to base10
    for i in str_num[::-1]:
        if i == '-':
            neg = True 
            continue 
        base10 += int(i) * b1 ** pow 
        pow += 1 

    #convert base10 to b2 
    while base10: 
        digit = base10 % b2
        res += conversion[digit] if conversion.get(digit) else str(digit)
        base10 //= b2

    return ('-' if neg else '') + (res[::-1])


### TEST CASE 
print (base_conversion('-615', 7, 13))
print (base_conversion('615', 10, 9))

