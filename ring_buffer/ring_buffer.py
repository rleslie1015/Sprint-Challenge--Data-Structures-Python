class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.front = None
        self.rear = None
        self.size = 0

    def append(self, item):
        new_node = Node(item)
        if self.size == self.capacity: # at capacity
            old_node = self.front # storing the value of the node to delete
            self.rear.next = new_node
            self.front = self.front.next
            old_node.next = None
            old_node = None
        elif self.front == None:
            self.front = new_node
            self.size +=1
        else: 
            self.rear.next = new_node
            self.size +=1
        self.rear = new_node
        self.rear.next = self.front
       

    def get(self):
        values = []
        curr = self.front
        while curr:
            values.append(curr.value)
            curr = curr.next
            if curr == self.front:
                break
        return values

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')
buffer.append('d')

print(buffer.get())  # should return ['a', 'b', 'c'] 

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']
