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
        # if list is at capacity
        if self.size == self.capacity: 
            # store the value of the node to delete
            old_node = self.front 

            # add the new node by making it the old rear's pointer 
            self.rear.next = new_node 

            # change the front pointer to next node
            self.front = self.front.next #at this point front is the second node in the ring 
            
            # disconnect the first node to remove it from the ring
            old_node.next = None
            # delete the node entirely ?????
            old_node = None
        # if ring is empty
        elif self.front == None:
            self.front = new_node
            # increase counter
            self.size +=1
        # if the list is not empty and not at capacity
        else: 
            # insert it after the rear
            self.rear.next = new_node
            # increase counter
            self.size +=1
        # update the pointers
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
