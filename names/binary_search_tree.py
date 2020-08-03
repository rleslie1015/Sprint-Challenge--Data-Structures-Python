from collections import deque
"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
# from queue import Queue
# from stack import Stack

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if value is less than
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else: 
                self.left.insert(value)
        # if value is more than
        elif value >= self.value:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if curr node matches target
        if self.value == target:
            return True
        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # recursive approach
        if not self.right:
            return self.value
        return self.right.get_max()

            # iterative approach
        # current = self
        # while current.right:
        #     current = current.right
        # return current.value


    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)
        if self is None:
            return
        if self.left is not None:
            self.left.for_each(fn)
        if self.right is not None:
            self.right.for_each(fn)




    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.left:
            self.left.in_order_print()

        print(self.value)

        if self.right:
            self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        # create a queue for nodes
        qq = deque()
        # add first node to the queue
        qq.append(self)
        # while queue is not empty
        while len(qq) > 0:
            # remove the first node from the queue
            curr = qq.popleft()
            # print the removed node
            print(curr.value)
            # add all children into queue
            if curr.left:
                qq.append(curr.left)
            if curr.right:
                qq.append(curr.right)
            

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # create a stack for nodes
        stack = []
    #     #  add the first node to the stack
        stack.append(self)
    #     # while stack is not empty 
        while len(stack) > 0:
    #       # get the current node from the top of the stack
            curr = stack.pop()
    #         #  print that node
            print(curr.value)
    #         # add all children to the stack 
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        print(self.value)
        if self.left:
            self.left.pre_order_dft()
        if self.right:
            self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self.left:
            self.left.post_order_dft()
        if self.right:
            self.right.post_order_dft()

        print(self.value)

"""
This code is necessary for testing the `print` methods
"""
# bst = BSTNode(1)

# bst.insert(8)
# bst.insert(5)
# bst.insert(7)
# bst.insert(6)
# bst.insert(3)
# bst.insert(4)
# bst.insert(2)

# bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.post_order_dft()
# print("post order")
# bst.post_order_dft()  


# # max_node = bst.get_max()
# # print(max_node)

# arr = []
# cb = lambda x: arr.append(x)
# bst.for_each(cb)