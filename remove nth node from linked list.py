##brute force soln
def removal(n,head):
    temp=head
    length=0
    new_head=0
    while temp is not None:
        length+=1
        temp=temp.next
    if length==n:
        new_head=head.next
        del head
        return new_head
    pos_to_stop=length-n
    temp=head
    count=1
    while count<pos_to_stop:
        temp=temp.next
        count+=1
    temp.next=temp.next.next

    return head
##optimal

def opti(n,head):
    slow=head
    fast=head
    for _ in range(n):
        fast=fast.next
    if fast==None:
        return head.next
    while fast.next is not None:
        slow=slow.next
        fast=fast.next
    slow.next=slow.next.next
    return head
