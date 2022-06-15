'''
Write a program  that takes the head of a singly linked list
If not cyclical, return null
If cyclical, return the node at the start of the cycle
'''
import llists

def test_cyclicity (l: llists.ListNode): 
    #Concept: create a hashtable of visited nodes. If there is a repeated node, return the first repeated node
    hash = []
    while l: 
        #add to hash
        hash.append(l)
        #step forward
        l = l.next
        #if in hash, break an return 
        if l in hash:
            return l 
    return None  

def test_cyclicity_rabbit_vs_turtle (l: llists.ListNode): 
    # Concept: have two walking pointers, a rabbit and a turtle. 
    # Cyclicity = True... if they coincide on the same node
    # Cyclicity = False.... if they don't coincide and the turtle = none
    def cycle_len(end): 
        # Concept: find the number of node steps in a cycle by noting the start and walking till return
        # 1. take a node within the cycle
        # 2. keep walking it forward until it returns to its original position
        start, step = end, 0
        while True: 
            step += 1
            start = start.next 
            if start == end:
                return step 
    rabbit = turtle = llists.ListNode(0, l)
    while rabbit and rabbit.next:
        turtle, rabbit = turtle.next , rabbit.next.next #rabbit jumps forward twice, turtle moves forward once 
        if rabbit == turtle:
            # Concept: create 2 iterators, one shifted by the cycle length (i.e. moving the lead to the tail) and the other starting at the head (ie. at the lead). 
            # Walk both iterators tandem. they will meet at the junction of the loop.
            # Why? because both have the same gap to the junction. 
            iter = shifted_iter = l
            for _ in range(cycle_len(turtle)):
                shifted_iter = shifted_iter.next
            while iter != shifted_iter:
                iter, shifted_iter = iter.next, shifted_iter.next 
            return iter
    return False 


### Test Cases 
a = llists.create_from_list([i for i in range(3,13)])
b = llists.create_from_list([i for i in range(3,13)])

a.next.next.next.next.next.next.next.next = a.next.next.next

print (test_cyclicity_rabbit_vs_turtle(a))
print (test_cyclicity_rabbit_vs_turtle(b))


### Learning Questions 

