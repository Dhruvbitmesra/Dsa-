class Solution(object):
    def hasCycle(self, head):
        visited = set()
        temp = head

        while temp is not None:
            if temp in visited:
                return True
            visited.add(temp)
            temp = temp.next

        return False



##def opti

def opti(object):
    slow=head
    fast=head
    while fast is not None and fast.next is not None:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            return True
    
    return false