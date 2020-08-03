class Node:
    def __init__(self, value):
        self.value = value
        self.next = None 

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_next(self, new_next):
        self.next = new_next
    
class LinkedList:
    def __init__(self, head=None, tail=None):
        self.head = head
        self.tail = tail

    def add_to_tail(self, value):  
        # create the Node from the value
        new_node = Node(value)

        if self.head is None and self.tail is None:
            # set the new node to be the tail
            self.head = new_node
            self.tail = new_node
        else:    
        # set the old tails next to refer to the new Node
            self.tail.set_next(new_node)
        # reassign
        self.tail = new_node

    def add_to_head(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head = new_node
        
    def remove_tail(self):
        # if we have a non empty linked list
        if self.head is None and self.tail is None:
            return
        # to find the second to last we start at the head until we get there
        current = self.head
        while current.get_next() is not self.tail:
            current = current.get_next()
            # at this point current is the node right before tail
        val = self.tail.get_value()
        # move self.tail to node right before
        self.tail = current
        return val

    def remove_head(self):
        # if we have a non empty linked list
        if self.head is None and self.tail is None:
            return None
        # if we only have a single elelment in the linked list
        if not self.head.get_next():
            head = self.head.get_value() # store value
            self.head = None
            self.tail = None
            return head
        val = self.head.get_value() # store value of head
        # move self.head to node right after
        self.head = self.head.get_next()
        # set head to be none
        return val

    def contains(self, value):
        current = self.head
        if self.head:
            while current.get_next():
                current = current.get_next()
                if current.get_value() == value:
                    return True
        else:
            return False

    def get_max(self):
        if not self.head:
            return None 
        max_value = self.head.get_value()
        current = self.head
        while current:
            if current.get_value() > max_value:
                max_value = current.get_value()
            current = current.next
        return max_value
        
    



