'''
Implement a Queue using stacks. 
Ensure FIFO principles 
'''


class Queue():
    # Initialize
    def __init__(self):
        # Concept: create two lists, one which is enqueue, the other which is dequeued
        self._enq = []
        self._deq = []

    @property
    def _header(self):
        return self._deq[-1] if self._deq else self._enq[0]

    @property
    def _tail(self):
        return self._enq[-1] if self._enq else self._deq[0]

    def __str__(self):
        return str(f'enq: {self._enq}\ndeq: {self._deq}')

    # Method: length
    def element_count(self):
        return (len(self._deq) + len(self._enq))

    # Method: enqueue
    def enqueue(self, x):
        self._enq.append(x)

    # Method: dequeue
    def dequeue(self):
        # Concept: pop from dequeue.
        # 1. if empty, pop enqueue items to deque
        # 2. if still empty, return error. list is empty!
        if not self._deq:
            while self._enq:
                self._deq.append(self._enq.pop())
        if not self._deq:
            raise IndexError('stacks are empty')
        return self._deq.pop()

# TEST CASES


a = Queue()
print(a)

print('\n# Test number of elements')
for i in range(3):
    a.enqueue(i)
print('elem count:', a.element_count())
print('head: ', a._header)
print('tail: ', a._tail)
print(a)

print('\n# Test resizing')
for i in (list('hello')):
    a.enqueue(i)
print('elem count:', a.element_count())
print('head: ', a._header)
print('tail: ', a._tail)
print(a)


print('\n # Test dequeue')
for _ in (range(3)):
    print('removed: ', a.dequeue())
    print(a)
