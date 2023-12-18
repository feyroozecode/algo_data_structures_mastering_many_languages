#Exercise 1: Linked List Reversal
#Problem Statement:
# Implement a function to reverse a linked list. 
# Your function should take the head of the linked list as input 
# and return the new head of the reversed linked list.

#Example: Input: 1 -> 2 -> 3 -> 4 -> 5  ==> Output: 5 -> 4 -> 3 -> 2 -> 1
class LinkedListClasser:
    def __init__(self, value):
        self.value = value
        self.next  = None
    
        
    def linked_list_classer(self, head):    
        if head is None or head.next is None:
           return head
       
        # init pointers
        current  = head
        previous = None
        nextNode = None 
        
        while current is not None:
            nextNode = current.next     # saving the next 
            current.next = previous     # reverse the next pointers
            previous     = current      # Move the previous to the current 
            current      = nextNode     # move the current pointer to nextNode  
        
        # the previous pointer now pointing to the new head
        return previous

# Usage Test
# Usage Test
# Create linked list nodes
node5 = LinkedListClasser(5)
node4 = LinkedListClasser(4)
node3 = LinkedListClasser(3)
node2 = LinkedListClasser(2)
node1 = LinkedListClasser(1)

# Link the nodes together
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Create an instance of LinkedListClasser
linked_list = LinkedListClasser(None)

# Call the linked_list_classer method
new_head = linked_list.linked_list_classer(node1)

# Print the reversed linked list
current = new_head
while current is not None:
    print(current.value, end=" -> ")
    current = current.next