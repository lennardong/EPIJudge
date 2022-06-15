'''
Implement a queue API using an array for storing elements. 
It is a constructor function

Initialization
- initial capacity of queue

Methods
- enqueue functions 
- dequeue fuctions 
- function for number of elements stored 

Notes
- the Class should dynamically resize to suport arbitrarily large size of elements 
'''

class Queue(): 
    SCALE_FACTOR = 2 #variables can be stored in the class. To call it, invoke the class object. Queue.SCALE_FACTOR

    def __init__(self, size: int):
        # input: size of elements
        # Concept
        # 1) create an empty list with X none elements 
        # 2) initialize variables: head, tail, number of elements 
        self._container = [None] * size
        self._head = self._tail = self._elementCount = 0 

    def __str__(self): 
        return str(self._container)

    def element_count(self) -> int:
        # Returns the number of elements within a circular queue
        return self._elementCount 
    
    def enqueue(self, element): 
        # Concept: private method to dynamically reize a container
        # 1. recalibrate container contents
        # 2. enlarge it 
        # 3. reset counters (head, tail)
        def resize():
            self._container = self._container[self._head:] + self._container[:self._head]
            self._head, self._tail = 0, self._elementCount
            self._container += [None] * (
                Queue.SCALE_FACTOR * len(self._container) - len(self._container))
            print (f'CONTAINER RESIZED: {len(self._container)}')
        
        # Concept: check if container is full and resize if needed. 
        if self._elementCount == len(self._container):
            resize()
        
        # Concept: add items and move numbers accordingly 
        # 1. assign to tail position 
        # 2. increase counters, checking for circularity. 
        # (note) do not worry about occupying a filled idx, this would be taken care in container size check
        self._container[self._tail] = element 
        self._elementCount += 1 
        print (f'ENQUEUE: {element} added to location {self._tail}.')
        self._tail = (self._tail + 1) % len(self._container) 

    def dequeue(self): 
        # Concept: remove the head item and return it  
        # 1. return and remove item at idx(head) by assigning it as "None"
        # 2. resize head, checking for circularity using mod
        self._elementCount -= 1 
        res = self._container[self._head]
        self._container[self._head] = None 
        self._head = (self._head + 1) % len(self._container)
        return res 

### TEST CASES 

a = Queue(5)
print (a)

print ('\n# Test number of elements')
for i in range(3):
    a.enqueue(i)
print ('elem count:', a.element_count())
print ('head: ', a._head)
print ('tail: ', a._tail)
print (a)

print ('\n# Test resizing')
for i in (list('hello')):
    a.enqueue(i)
print ('elem count:', a.element_count())
print ('head: ', a._head)
print ('tail: ', a._tail)
print (a)


print ('\n # Test dequeue')
for _ in (range(3)): 
    print ('removed: ', a.dequeue())
    print (a)



### Questions
'''
Q: how do you invoke a variable within the class? 

Q: does a private method (i.e. nested in a class method) need to invoke (self) as an argument? 

'''