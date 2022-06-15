import random 

class Stack(): 
    #init 
    def __init__(self): 
        self._element_with_max = [] #key = element, value = current max 
    
    def __str__(self):
        res = [] 
        for dict_item in self._element_with_max:
            res.append(dict_item.get('element'))
        return str(res)

    #empty 
    def empty(self): 
        return len(self._element_with_max) == 0 

    #max
    def max(self): 
        if self.empty():
            raise IndexError ('max(): empty stack')
        return self._element_with_max[-1].get('max')

    #pop
    def pop(self):
        if self.empty():
            raise IndexError ('pop(): empty stack')
        return self._element_with_max.pop().get('element')

    #push
    def push(self, x): 
        prev_max = self._element_with_max[-1].get('max') if not self.empty() else x
        self._element_with_max.append(
            {'element': x,
            'max': max(x, prev_max)}
        )

class Stackv2(): 
    '''Implementing with an independant cache
    
    Concept: 
    1. Cache tracks the standing max numbers and their number of occurances
    2. If number is 0, item is popped
    '''
    def __init__(self): 
        self._element = []
        self._max_w_count = {} #Key(maxvalue) : Value (count)
    
    def __str__(self): 
        return str(self._element)

    def push(self, n: int):
        ### add element
        self._element.append(n)

        ### assess max w count 
        # if empty , add it 
        if len(self._max_w_count) == 0: 
            self._max_w_count[n] = 1
        # if a new max, add it 
        elif n not in self._max_w_count and max(self._max_w_count.keys()) < n: 
            self._max_w_count[n] = 1
        #if equal, add count 
        elif n in self._max_w_count: 
            self._max_w_count[n] += 1 
        # if less, leave alone 

    def empty(self): 
        return len(self._element) == 0
    
    @property
    def max(self):
        if self.empty():
            raise IndexError('max(): empty stack')
        return list(self._max_w_count.keys())[-1]
    
    def pop(self):
        # remove element 
        val = self._element.pop()
        
        # check for element membership in cache
        if val in self._max_w_count:
            self._max_w_count[val] -= 1
            
            #if zero, then remove 
            if self._max_w_count[val] <= 0: 
                del self._max_w_count[val] 
            
        return val 

### TEST CASES 
print ('-------v1---------')
a = Stack()
for i in range(100):
    x = random.randint(0,1000)
    a.push(x)

print(a.max())
print (a)
print(a._element_with_max[-1])

print ('-------v2---------')
b = Stackv2()
for i in range(100):
    x = random.randint(0,1000)
    b.push(x)

print(b.max)
print(b)

## QUESTIONS 

# Q: Why must dict.value be passed into list() to iterate over it? 
# A: dict.value() is a 'view object'. 

# Q: Why is this syntax invalid: del self._max_w_count[val] if self._max_w_count[val] <= 0