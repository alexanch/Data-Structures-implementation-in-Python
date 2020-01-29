class Element(object):
    """
    Element class represents a single unit in a linked list
    """
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList(object):
    """
    LinkedList class represents a linked list.
    """
    def __init__(self, head=None):
        self.head = head
    
    def append(self, new_element):
        """ 
        Add a new Element to the end of LinkedList.
        """
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element
     
     def get_position(self, position=1):
        """
        Get an element from a particular position.
        """
        k = 1 
        current = self.head
        while k!=position:
            if current.next == None:
                return None
            else:
                current = current.next
                k+=1
        return current
    
    def insert(self, new_element, position = 1):
        """
        Insert a new node at the given position.
        """
        current = self.head
        k = 1
        while k!=position-1:
            current = current.next
            k+=1
        else:
            temp = new_element
            self.temp = temp
            self.temp.next = current.next
            current.next = self.temp
        
        
    def delete(self, value):
        """
        Delete the first node with a given value.
        """
        if self.head.value == value:
            self.head = self.head.next
        else:
            current = self.head
            while current.next.value != value:
                current = current.next
            else:
                current.next = current.next.next
                
                
                
                
                
"""                
# Test cases:
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
"""
