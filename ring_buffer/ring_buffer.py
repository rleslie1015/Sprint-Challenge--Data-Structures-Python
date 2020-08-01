from singly_linked_list import LinkedList
from singly_linked_list import Node
class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = LinkedList()


    def append(self, item):
        #  create new node 
        new_node = Node(item)
        #  move head pointer to the new_nodes next
        self.storage.head = new_node.next
        # checking if the front has an item to overwrite
        if self.storage.head:
            # overwrite the fron with new_node
            self.storage.head = new_node
        else:
            #  assign tail pointer to the new node 
            self.storage.tail = new_node




    def get(self):
        values = []
        current = self.storage.tail
        while current.next is not self.storage.head:
            if current.value is not None:
                values.append(current.value)
            current = current.prev
        print(*values, sep=", ")
        return values

buffer = RingBuffer(3)

buffer.get()   # should return []

buffer.append('a')
buffer.append('b')
buffer.append('c')

print(buffer.get())  # should return ['a', 'b', 'c']

# # 'd' overwrites the oldest value in the ring buffer, which is 'a'
# buffer.append('d')

# buffer.get()   # should return ['d', 'b', 'c']

# buffer.append('e')
# buffer.append('f')

# buffer.get()   # should return ['d', 'e', 'f']
