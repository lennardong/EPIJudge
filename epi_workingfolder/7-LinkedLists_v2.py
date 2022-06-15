class Node():
    def __init__(self, data):
        self.data = data 
        self.next = None
    #def __str__(self):
     #   return str(self.data) + ' -> ' + str(self.next)
    def __repr__(self):
        return f'{self.data} -> {self.next.data}'

class LinkedLists(): 
    def __init__(self, nodes: list = None): 
        self.head = None
        if nodes is not None: #this so we don't pollute the original class pointer
            node = Node(nodes.pop(0))
            self.head = node
            #print ('nodes is not None: ', str(self.head))
            for n in nodes: 
                node2 = Node(n)
                node.next = node2
                node = node2 
                #print('elem in node:', str(node))

    def __repr__ (self): 
        node = self.head
        nodes = [] 
        while node is not None: #while the pointer is still pointing
            nodes.append(str(node.data))
            node = node.next
        nodes.append('None')
        return ' -> '.join(nodes)
    
    def __iter__(self): 
        current = self.head
        while current: 
            yield current
            current = current.next
    
    def __len__(self):
        count = 0
        node = self.head
        while node: 
            count += 1 
            node = node.next 
        return count 
    
    def add_node(self, value): 
        if self.head is None: 
            self.head = Node(value)
        else: 
            self.tail 
    
    @property
    def values(self):
        return [node.data for node in self]
    
    def add_node_at(self, node: Node, new_node: Node): 
        n = self.find_node(node)
        new_node.next = n.next 
        n.next = new_node 
        return self 
                
    def find_node(self, data):
        node = self.head 
        while node.data != data:
            node = node.next 
        return node 
    
    def delete_node(self, data):
        
        '''
        concept: replace preceeding pointer with current pointer 
        # A B C 
        # A C 
        '''

        for node in self: #search and have a cache for prev item 
            if node.next.data == data: #issue here is they are different types. node.next is type Class(Node). We need to access its information, thus, Node.next.data 
                node.next = node.next.next
                break 
        return self 
        
## DEBUGGING
llist = LinkedLists()
first_node = Node('A')
second_node = Node('B')
first_node.next = second_node
llist.head = first_node

llist2 = LinkedLists([1,3,2,4,5])
'''
print (llist2)
print ('len: ',len(llist2))
print ('find:', llist2.find_node(3))
print ('add_node_at:', llist2.add_node_at(3, Node(9)))
'''
print ('delete_node:', llist2.delete_node(3))

# The only item that lives in the linkedlist class is the head. 