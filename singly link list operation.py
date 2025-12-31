class Node:
    def __init__(self,val):
        self.val=val
        self.next=None



node1=Node(5)
node2=Node(10)
node3=Node(7)
node4=Node(8)

node1.next=node2
node2.next=node3
node3.next=node4


print(node1.next)
print(node2)


##append
class singlylinklist:
    def __init__(self):
        self.head=None
    def append(self,val):
        new_node=Node(val)
        if self.head==None:
            self.head=new_node
        else:
            curr=self.head
            while curr.next is not None:
                curr=curr.next
            curr.next=new_node

##traversal
    def traversal(self):
        if self.head is None:
            print("Sll is empty")
        else:
            curr=self.head
            while curr is not None:
                print(curr.val,end=" ")
                curr=curr.next

##insert most imp

    def insert_at(self,val,position):
        new_node=Node(val)
        if position==0:
            new_node.next=self.head
            self.head=new_node
        else:
            current=self.head
            prev_node=None
            count=0
            while current is not None and count<position:
                prev_node=current
                current=current.next
                count+=1
            prev_node.next=new_node
            new_node.next=current 

##delete
    def delete(self,val):
        temp=self.head
        if temp.next is not None:
            if temp.val==val:
                self.head=temp.next
                return
            else:
                found=False
                prev=None
                while temp is not None:
                    if temp.val==val:
                        found=True
                        break
                    prev=temp
                    temp=temp.next
                
                if found:
                    prev.next=temp.next
                    return
                else:
                    print("Node not found")









sll=singlylinklist()
sll.append(10)
sll.append(20)
sll.append(30)
sll.append(40)
sll.append(50)
sll.traversal()