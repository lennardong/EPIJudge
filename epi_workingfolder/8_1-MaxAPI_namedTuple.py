'''
implement a max api for a stack. 
'''
from random import randint
import collections

class Stack(): 
    # Create a tuple object
    element_with_max = collections.namedtuple('element_with_mmax', ('element', 'max'))

    #init 
    def __init__(self): 
        self._element_with_max = [] 
    
    def __str__(self):
        res = [] 
        for i in self._element_with_max:
            res.append(i.element)
        return str(res)

    #empty 
    def empty(self): 
        return len(self._element_with_max) == 0 

    #max
    def max(self): 
        if self.empty():
            raise IndexError ('max(): empty stack')
        return self._element_with_max[-1].max

    #pop
    def pop(self):
        if self.empty():
            raise IndexError ('pop(): empty stack')
        return self._element_with_max.pop().element

    #push
    def push(self, x): 
        self._element_with_max.append(
            self.element_with_max(x, 
            x if self.empty() 
            else max(x, self.max()))
        )    

### TEST CASE 

a = Stack()
#a.max() 
for i in range(100):
    x = randint(0,1000)
    a.push(x)

print(a.max())
print (a)
print(a._element_with_max[-1])
