##brute force soluton
"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        stack = []
        temp = head

        # Push values to stack
        while temp is not None:
            stack.append(temp.data)
            temp = temp.next

        temp = head

        # Replace values in reverse order
        while temp is not None:
            temp.data = stack.pop()
            temp = temp.next

        return head
    

##optimal solution


"""
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        if head.next is None:
            return head
        curr=head
        prev=None
        while curr is not None:
            front=curr.next
            curr.next=prev
            prev=curr
            curr=front
        return prev