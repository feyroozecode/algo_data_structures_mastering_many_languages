# Exercise 1: Linked List Reversal
# Exercise: Advanced Linked List Reversal
# Problem Statement:
# You are given a linked list where each node has two pointers:
# next: points to the next node in the list.
# random: points to a random node in the list, possibly null.
# Your task is to reverse the linked list in such a way that for every node, the next pointer points to the previous node, and the random pointer is also reversed accordingly.
# Implement a function to achieve this advanced reversal. Your function should take the head of the linked list as input and return the new head of the reversed linked list.

class Node :
    def __init__(self, value):
        self.value = value 
        self.next = None
        self.random = None
        
    
def advanced_linked_list_reversal(head):
    
    if head is None or head.next is None:
         return head 
     
     # Step 1: Reverse the next pointers 
     
    current  = head
    previous = None
    nextNode = None
     
    while current is not None:
        nextNode      = current.next
        current.next = previous 
        previous      = current
        current       = nextNode 
         
     # reverse head     
    current = head
    
    while current is not None:
        # abing a nextNode before modifying random pointer
        nextNode = current.next
         
        # reverse random pointer 
        current.next = previous
         
        current = nextNode
         
    return previous 

# Usage
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)

n1.next = n2
n2.next = n3
n3.next = n4

n1.random = n3
n2.random = n1
n3.random = n4


# Print the original linked list with random pointers
current = n1
while current:
    print(f"Value: {current.value}, Random: {current.random.value if current.random else None}")
    current = current.next

# Reverse the linked list
new_head = advanced_linked_list_reversal(n1)

# Print the reversed linked list with reversed random pointers
current = new_head
while current:
    print(f"Value: {current.value}, Random: {current.random.value if current.random else None}")
    current = current.next
