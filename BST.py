""" Binary Search Tree Implementation: search, insert, print methods. """

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_helper(self.root,new_val)

    def insert_helper(self,start,new_val):
        """
        Helper function for recursive insert method.
        """
        if new_val>start.value:
            if start.right:
                self.insert_helper(start.right,new_val)
            else:
                start.right = Node(new_val)
        elif new_val<start.value:
            if start.left:
                self.insert_helper(start.left,new_val)
            else:
                start.left = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root,find_val)
        
    def search_helper(self, start, find_val):
        """
        Helper function for recursive search method.
        """
        if start:
            if start.value == find_val:
                return True
            elif find_val>start.value:
                return self.search_helper(start.right,find_val)
            elif find_val<start.value:
                return self.search_helper(start.left,find_val)
        return False
            
    def print_tree(self):
        return self.print_helper(self.root)[:-1]
    
    def print_helper(self,next,traversal =''):
        """
        Helper function for recursive print method.
        """
        if next:
            traversal +=(str(next.value)+'-')
            traversal = self.print_helper(next.left, traversal)
            traversal = self.print_helper(next.right,traversal)
        return traversal
        
"""
Test case:

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
"""
