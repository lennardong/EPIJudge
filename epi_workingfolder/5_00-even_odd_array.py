def even_odd(A: list[int]) -> list[int]: 
    '''
    given A, sorts A into even and odd
    '''
    next_even, next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[next_even] % 2 == 0: #if even, move on
            next_even += 1 
        else: #if not even, its odd. Send to back and 
            A[next_even], A[next_odd] = A[next_odd], A[next_even]
            next_odd -= 1
        print (f'next even: {next_even}: {A[next_even]} | next odd: {next_odd}: {A[next_odd]}')
    return A

A = [i for i in range(13)]

print(even_odd(A))