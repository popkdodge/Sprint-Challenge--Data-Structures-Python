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
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # compare the input value with the value of the node
        # if value < Node's value
        if value < self.value:
            # we need to go left
            # if there is no left child we can park it
            if self.left is None:
            # if there' no node to compare the input value to, 
            # then we can wrap the value in a BSTNode and park it
                self.left = BSTNode(value)
            # otherwise there is a child on the left side already there
            else:
            # call the left child's insert method
                self.left.insert(value)
        # otherwise, value >= Node's value
        else:
            # we need to go right
            # if we see tehre is no right child, then we can wrap the value
            if self.right is None:
            # in a BSTNode and park it.
                self.right = BSTNode(value)
            # otherwise there is a child on the right side
            else:
                # call teh right child 'insert' method
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # check if value exist!
        if target == self.value:
            return True
        if target > self.value and self.right:
            return self.right.contains(target)
        if target < self.value and self.left:
            return self.left.contains(target)
        return False

    # Return the maximum value found in the tree
    def get_max(self):
        if self.value is not None and self.right is None:
            return self.value
        if self.right:
            node = self.right
            while node.right is not None:
                node = node.right
            return node.value
        

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        if self.value:
            fn(self.value)          
            if self.right:          
                self.right.for_each(fn)         
            if self.left:           
                self.left.for_each(fn)          



    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self:
            if self.left:
                self.left.in_order_print()
            print(self.value)
            if self.right:
                self.right.in_order_print()

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    

    def bft_print(self):
        from collections import deque
        # BFT: FIFO
        # we'll use a queue to facilitate the ordering of the elements
        queue = deque()
        queue.append(self)

        # continue to traverse so long as tehre are nodes in the queue

        while len(queue) > 0 :
            current = queue.popleft()

            if current.left:
                queue.append(current.left)
            
            if current.right:
                queue.append(current.right)
            
            print(current.value)


    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        # DFT: LIFO
        # we'll use a stack
        stack = []
        stack.append(self)

        # so long as our stack has nodes in import 
        # there are more node to traverse

        while len(stack) > 0 :
            # pop the top node form the stack
            current = stack.pop()

            # add teh current node's right child first
            if current.right:
                stack.append(current.right)
            # add the currend node's left child
            if current.left:
                stack.append(current.left)

            print (current.value)
    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        if self is not None:
            print(self.value)
            if self.left:
                self.left.pre_order_dft()
            if self.right:
                self.right.pre_order_dft()

    # Print Post-order recursive DFT
    def post_order_dft(self):
        if self is not None:
            if self.left:
                self.left.post_order_dft()
            if self.right:
                self.right.post_order_dft()
            print(self.value)

    def in_order_dft(self):
        if self is not None:
            if self.left:
                self.left.in_order_dft()
            print(self.value)
            if self.right:
                self.right.in_order_dft()

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

bst.bft_print()
bst.dft_print()

print("elegant methods")
print("pre order")
bst.pre_order_dft()
print("in order")
bst.in_order_dft()
print("post order")
bst.post_order_dft()  
