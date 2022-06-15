'''
Given a singly linked list and an integer k, 
write a program to remove the kth last element from the list
You cannot assume that it is possible to record the length of the list
'''
import llists

def remove_k (l: llists.ListNode, k: int) -> llists.ListNode: 
    # Concept: tow truck. imagine 2 iterators, a lead and lagging iterator. 
    # The lagging iterator is behind the lead by k+1 steps. therefore, when the lead iterator reaches the end, the lagging iterator will be at kth last element
    # Remove 
    lead_iter = lag_iter = llists.ListNode(0,l)
    count = 0 
    while lead_iter: 
        count, lead_iter = count + 1 , lead_iter.next 
        lag_iter = lag_iter.next if count > k + 1 else lag_iter
    removal = lag_iter.next 
    lag_iter.next = lag_iter.next.next 
    return removal
    

### TEST CASES 
b = [i for i in range(20, 0 ,-1)]
print (b)

a = llists.create_from_list(b)
llists.print_chain(a)

print(type(remove_k(a, 12)))
#llists.print_chain(a)
