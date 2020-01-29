""" Binary tree implementation. """

class Node(object):    
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """
        Returns True if the value is in the tree, 
        otherwise: return False.
        """
        find_val = int(find_val)
        if self.root.value == find_val:
            return True
        else:
            if self.root.left:
                x = self.preorder_search(self.root.left,find_val)
            if self.root.right and x != True:
                f = self.preorder_search(self.root.right,find_val)        
                return f 
            else:
                return x
            
    def preorder_search(self, start, find_val):
        """
        Helper method to create a 
        recursive search solution.
        """
        if start.value == find_val:
            return True
        else:
            if start.left:
                xx = self.preorder_search(start.left, find_val)
                if xx == True:
                    return True
              
            if start.right and xx!=True:
                yy = self.preorder_search(start.right,find_val)
                if yy == True:
                    return True   
            
            return False
                
    def preorder_print(self, start, traversal=[]):
        """
        Helper method to create a 
        recursive print solution.
        """
        traversal.append(str(start.value))
        if start.left:
            self.preorder_print(start.left, traversal)
        if start.right:
            self.preorder_print(start.right, traversal)
        return traversal
        
    def print_tree(self):
        """
        Print out all tree nodes as they are
        visited in a pre-order traversal.
        """
        if self.root.value:
            return '-'.join(self.preorder_print(self.root))
        else:
            return 'Empty'

"""
Test case:
# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)

# Test print_tree
# Should be 1-2-4-5-3
print tree.print_tree()
"""
