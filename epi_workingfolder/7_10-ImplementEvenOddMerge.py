'''
Consider a singly linked lists where nodes are numbered starting at 0
define the list to be consisting of even numbered nodes then odd numbered nodes 
'''
import llists 

def even_odd_merge(l: llists.ListNode) -> llists.ListNode: 
    '''Takes a list and organizes it into even and odd sublists. based on node position, not node content
    
    Starts 2 new linkedlists (even / odd) and joins them at the end of the process 
    Uses 3 iterators: to route the nodes 

    Arguments:
        l: head node of list to be sorted 

    Returns:
        headnode of sorted lists 
    '''
    even_iter, odd_iter, pri_iter = llists.ListNode(0), llists.ListNode(0), l
    even_head = even_iter
    odd_head = odd_iter

    while l and l.next: 
        pri_iter = l
        #cut and paste
        even_iter.next = pri_iter
        odd_iter.next = pri_iter.next 
        # Iterate through the list 
        l = l.next.next if l.next is not None else None 
        even_iter = even_iter.next
        odd_iter = odd_iter.next 
    
    #edge case: if length of l is odd
    if l: 
        even_iter.next = l
        even_iter = even_iter.next 
    
    #join the two 
    even_iter.next = odd_head.next
    odd_iter.next = None

    return even_head.next 
    

### TEST CASES 
a = llists.create_from_list([i for i in range(20)])
llists.print_chain(a)
llists.print_chain(even_odd_merge(a))


### QUESTIONS 

# Q: what is ^= 1 