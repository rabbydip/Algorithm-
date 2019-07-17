class node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
        self.last_node=None
    def append(self,data):
        if self.last_node is None:
            self.head=node(data)
            self.last_node=self.head
        else:
            self.last_node.next=node(data)
            self.last_node=self.last_node.next
            
    def display(self):
        current=self.head
        while current is not None:
            print(current.data,end=' ')
            current=current.next

mylist=linklist()
n=int(input("enter the number of elements:"))
for i in range(n):
    data=int(input())
    mylist.append(data)
mylist.display()
