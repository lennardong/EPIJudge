import llists

def merge_two_sorted_lists(l1, l2):
    '''
    Create a dummy header, which which we will use in the first while and leave behind. it will to point to the first object. 
    Create a dummy tail, which will walk along the while loops and thread through all the objects and rewrite their pointers
    Thread L1 and L2 till one is exhausted, then point to the remaining L1 or L2 element so it stretches on
    
    Learning: Variables are only "handles" to access the ListNode. No new data is created. 
    '''
    header = tail = llists.ListNode()
    while l1 and l2: 
        if l1.data <= l2.data: 
            tail.next, l1 = l1, l1.next 
        else:
            tail.next, l2 = l2, l2.next
        tail = tail.next 
    
    tail.next = l1 if l1 is not None else l2
    return header.next   


### TEST CASES

#list a
lla1 = llists.ListNode(2)
lla2 = llists.ListNode(5)
lla3 = llists.ListNode(7)
a = [lla1, lla2, lla3]
for idx, node in enumerate(a):
    node.next = a[idx + 1] if idx < len(a) - 1 else None 
#list b
llb1 = llists.ListNode(3)
llb2 = llists.ListNode(6)
llb3 = llists.ListNode(11)
llb4 = llists.ListNode(23)
b = [llb1, llb2, llb3, llb4]
for idx, node in enumerate(b):
    node.next = b[idx + 1] if idx < len(b) - 1 else None 
#test
test = merge_two_sorted_lists(lla1, llb2)
llists.print_chain(test)
print(repr(llb1))

    