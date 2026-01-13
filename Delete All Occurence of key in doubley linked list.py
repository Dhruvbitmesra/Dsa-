##one and only optimal solution
def delete(node,head,k):
    if head.next is None and head.val==k:
        return None
    temp=head
    prev=None
    new_head=head
    while temp is not None:
        if temp.val==k:
            if prev is not None:
                prev.next=temp.next
            if temp.next is not None:
                temp.nexxt.prev=prev
            if temp==new_head:
                new_head=new_head.next
        prev=temp
        temp=temp.next
    return new_head