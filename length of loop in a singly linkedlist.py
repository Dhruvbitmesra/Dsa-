# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCyclelength(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        temp=head
        travel=0
        my_dict=dict()
        while temp is not None:
            if temp in my_dict:
                return travel-my_dict[temp]


            my_dict[temp]=travel
            travel+=1
            temp=temp.next

        return 0
    


##def optimal solution of  this 
class Solution(object):
    def detectCyclelength(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow=head
        fast=head
        while fast is not None and fast.next is not None:
            slow=slow.next
            fast=fast.next.next
            if slow==fast:
                slow=slow.next
                count=1
                while slow!=fast:
                    slow=slow.next
                    count+=1
                return count
            
            
            
        return 0
    



  

        
        


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def create_cyclic_linked_list(values, pos):
    if not values:
        return None

    head = ListNode(values[0])
    current = head
    cycle_node = None

    for i in range(1, len(values)):
        current.next = ListNode(values[i])
        current = current.next
        if i == pos:
            cycle_node = current

    if pos != -1:
        current.next = cycle_node

    return head


def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# Example
head = create_cyclic_linked_list([1, 2, 3, 4, 5], pos=2)
print(hasCycle(head))  # True
