# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        cycle=set()
        temp=head
        while temp is not None:
            if temp in cycle:
                return temp
            cycle.add(temp)
            temp=temp.next
         
        