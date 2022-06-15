import random 

class Stack(): 
    #init 
    class MaxCount():
        def __init__(self, element, max):
            self.element = element
            self.max = max 
        def __str__(self): 
            return str(self.element)

    def __init__(self): 
        self._element_with_max = [] 
    
    def __str__(self):
        res = [] 
        for item in self._element_with_max:
            res.append(item.element)
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
        prev_max = self._element_with_max[-1].max if not self.empty() else x
        self._element_with_max.append(self.MaxCount(x, max(x, prev_max)))

### TEST CASES 
a = Stack()
#a.max() 
for i in range(100):
    x = random.randint(0,1000)
    a.push(x)

print(a.max())
print (a)
print(a._element_with_max[-1])
