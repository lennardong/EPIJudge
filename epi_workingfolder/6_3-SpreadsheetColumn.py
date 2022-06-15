import string 

def spreadsheet_column(col: str) -> int: 
    '''
    Takes in a string and outputs the col no ord()
    '''

    pow, res = 1, 0 
    letters = '-' + string.ascii_uppercase
    col = list(col.upper())

    while col: 
        res += letters.index(col.pop()) ** pow
        pow += 1
    return res 

## TESTCASE 
print (spreadsheet_column('D'), '4')
print (spreadsheet_column('AA'), '27')
print (spreadsheet_column('ZZ'), '702')