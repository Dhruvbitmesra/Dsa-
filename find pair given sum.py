##brute solution
from typing import Optional


from typing import List

"""

Definition for singly Link List Node
class Node:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

You can also use the following for printing the link list.
displayList(node)
"""

from typing import Optional, List

class Solution:
    def findPairsWithGivenSum(self, target: int, head: Optional['Node']) -> List[List[int]]:
        temp1 = head
        st = set()

        while temp1 is not None:
            temp2 = temp1.next
            while temp2 is not None:
                if temp1.data + temp2.data == target:
                    st.add((temp1.data, temp2.data))
                temp2 = temp2.next
            temp1 = temp1.next

        # sort pairs by first element, then second
        result = sorted(st)
        return [list(pair) for pair in result]



#optimal
def opti(head,target):
    result=[]
    left=head
    right=head
    while right.next is not None:
        right=right.next

    while left.next is not None and right.prev is not None and left.data<right.data:
        total=left.data+right.data
        if total==target:
            result.append([left.data,right.data])
            left=left.next
            right=right.prev
        elif total>target:
            right=right.prev
        else:
            left=left.next

    return result