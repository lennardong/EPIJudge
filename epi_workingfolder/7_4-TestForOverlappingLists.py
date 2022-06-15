import llists

def is_overlapping_nested(a: llists.ListNode,b: llists.ListNode) -> bool: 
    # Concept: use a nested loop in a. 
    # 1. loop through a
    # 2. for each item in a, check if b == a 
    while a: 
        while b: 
            print (f'a: {a}, b: {b}')
            if b == a: 
                return True 
            b = b.next 
        a = a.next #to check: why won't this loop? 
    return False 


def is_overlapping_shifted (a: llists.ListNode, b: llists.ListNode) -> bool: 
    # Concept: to shift the lists to equal distances from a convergence, if there is one 
    # 1. find the lengths
    # 2. walk the longer list forward by difference of lengths 
    # 3. walk both lists in tandem. return True if they converge 
    def find_length (start):
        count = 0 
        while start: 
            count += 1 
            start = start.next 
        return count 

    len_a, len_b = find_length(a), find_length(b)
    longer_list = a if len_a >= len_b else b 
    shorter_list = a if len_a < len_b else b 

    for _ in range(abs(len_a - len_b)):
        longer_list = longer_list.next
    
    while longer_list and longer_list != shorter_list: 
        longer_list = longer_list.next 
        shorter_list = shorter_list.next
        
    return longer_list if longer_list == shorter_list else None 



### TEST CASE 
a = llists.create_from_list([i for i in range(10)])
b = llists.create_from_list([i for i in list('hello')])
b.next.next.next = a.next.next.next.next

llists.print_chain(a)
llists.print_chain(b)
print (is_overlapping_nested(a, b))
print (is_overlapping_shifted(a, b))

### LEARNING QUESTION 
# Q: What is the 3 steps to find if linked lists are overlapping 