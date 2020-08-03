"""
Each ListNode holds a reference to its previous node
as well as its next node in the List.
"""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

"""
Our doubly-linked list class. It holds references to 
the list's head and tail nodes.
"""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length
    
    def __str__(self):
        return f' head: {self.head.value} \n tail: {self.tail.value}, \nlength = {self.length}'
    """
    Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly.
    """
    def add_to_head(self, value):
        #  make new node
        new_node = ListNode(value)
        # check if list is empy 
        if not self.head:
            # assign new to head and tail
            self.head = new_node
            self.tail = new_node
        # else set the old head prev pointer to new node
        else:
            self.head.prev = new_node
            # set the new nodes next pointer to self.head
            new_node.next = self.head
            # assign self. head to new pointer
            self.head = new_node
        # update length 
        self.length += 1
        
    """
    Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node.
    """
    def remove_from_head(self):
        # if empty return None
        if not self.head:
            return None
        # if only one node in the list 
        if self.length == 1:
            # store the value of the node
            val = self.head.value
            # set tail and head to None
            self.head = None
            self.tail = None
            # set length to 0
            self.length = 0
            # return value
            return val
        # else (longer than one):
        else: 
            # store the value of the head
            val = self.head.value
            # assign the next node in the list to its own var (second_node)
            second_node = self.head.next
            # set second_node.prev to None
            second_node.prev = None
            # assign self.head to second Node
            self.head = second_node
            # length - 1
            self.length -= 1
            return val
            
    """
    Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly.
    """
    def add_to_tail(self, value):
        # create new node
        new_node = ListNode(value)
        # if list is empty:
        if not self.head and not self.tail:
            # assing self.head and tail to new_node
            self.head = new_node
            self.tail = new_node
            # update length
            self.length += 1
        # else 
        else:
            # assign the self tails next to new node
            self.tail.next = new_node
            # assign the new_nodes prev to self.tail
            new_node.prev = self.tail
            # reassing the tail to new node
            self.tail = new_node
            
            # update the length
            self.length += 1


            
    """
    Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node.
    """
    def remove_from_tail(self):
        # if list is empty
        if self.length < 1:
            # return None
            return None
        # elif list is only one node:
        elif self.length == 1:
            # store the value of the node
            val = self.tail.value
            # assign head and tail to none
            self.head = None
            self.tail = None
            # update length
            self.length -=1  
            # return value
            return val
        # else (list has more that one):
        else: 
            # store the value of self.tail
            val = self.tail.value
            # get the tails prev value (new_tail)
            new_tail = self.tail.prev
            # assign new.tail.next to None
            new_tail.next = None
            # set the tail to be new_tail
            self.tail = new_tail
            # update length
            self.length -=1  
            return val
    

            
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List.
    """ 
    def move_to_front(self, node):
        if self.head == node:
            return
        if self.tail == node: # if we want to move the tail
            # get the tail
            new_head = self.tail
            # update the next pointer 
            new_head.next = self.head
            # assign new tail
            self.tail = self.tail.prev
            #  assign new_ head 
            self.head = new_head
        # if list has more than one node 
        if self.length > 1:
            # make a current marker set to self.head
            current = self.head
            # while current is not node and current.next:
            while current is not node and current.next:
                # update current to next 
                current = current.next
                if current == node:
                    # place the previous and next node into variable
                    previous = current.prev
                    next_node = current.next
                    # set the next_node.prev to previous
                    next_node.prev = previous
                    # set the current.prev to None
                    current.prev = None
                    # set the current.next to self.head
                    current.next = self.head
                    # self.head to current
                    self.head = current     
     
    """
    Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List.
    """
    def move_to_end(self, node):
        if self.tail == node:
            return
        if self.head == node: # if we want to move the head
            new_tail = self.remove_from_head()
            self.add_to_tail(new_tail)
        else:
            new_tail_value = node.value
            self.delete(node)
            self.add_to_tail(new_tail_value)
              
    """
    Deletes the input node from the List, preserving the 
    order of the other elements of the List.
    """
    def delete(self, node):
        # if list has more than one node:
        if self.length == 1:
            self.head = None
            self.tail = None
            self.length = 0
        elif node is self.head:
            next_node = self.head.next
            # assign next_node to self.head
            self.head = next_node
            # assign self.head.prev to None
            self.head.prev = None
            self.length -=1
        elif node is self.tail:
            previous = self.tail.prev
            # reassign tail to previous
            self.tail = previous
            # assign previous.next to None
            self.tail.next = None
            self.length -= 1
        else: # ( node is not head or tail ):
            current = self.head
            while current and current.next:
                current = current.next
                if current == node:
                    # get the prev and after nodes and assign them to None variables
                    next_node = current.next
                    # previous = None
                    # if current.previous is not None:
                    previous = current.prev
                    # assign previous.next to next_node
                    previous.next = next_node
                    next_node.previous = previous
                    self.length -= 1
    """
    Finds and returns the maximum value of all the nodes 
    in the List.
    """
    def get_max(self):
        # if list has more than one node:
        max_value = self.head.value
        if self.length > 1:
            current = self.head
            while current:
                # if current is greater than max:
                if current.value > max_value:
                    # reassign max to current.value
                    max_value = current.value
                current = current.next
            return max_value
        elif self.length == 1:
            return self.head.value
    

# node = ListNode(1)
# ll = DoublyLinkedList(node)

# ll.add_to_head(40)
# ll.move_to_end(ll.head)
# ll.add_to_tail(4)
# # ll.add_to_tail(4)
# print(ll.head.next.value)
# ll.move_to_end(ll.head.next)
# print(ll)
# # ll.get_max()