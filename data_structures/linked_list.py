class Node:
    def __init__(self,data=0):
        self.data=data
        self.link=None
    def get_data(self):
        return self.data
    def set_data(self,new_data):
        self.data=new_data
    def get_link(self):
        return self.link
    def set_link(self,new_link):
        self.link=new_link
class LinkedList:
    def __init__(self):
        self.head=None
    def add(self,data):
        temp=Node(data)
        temp.set_link(self.head)
        self.head=temp
    def update(self,target,new_value):
        curr=self.head
        found=False
        while curr!=None and not found:
            if curr.get_data()==target:
                curr.set_data(new_value)
                found=True
            else:
                curr=curr.get_link()
        if found:
            print("Updated")
        else:
            print("Error updating")
    def delete(self,target):
        prev=self.head
        curr=self.head
        found=False
        while curr!=None and not found:
            if curr.get_data()==target:
                prev.set_link(curr.get_link)
                found=True
            else:
                prev=curr
                curr=curr.get_link()
        if found:
            print("Deleted")
        else:
            print("Error deleting")
    def size(self):
        curr=self.head
        count=0
        while curr!=None:
            count+=1
            curr=curr.get_link()
        return count
    def search(self,target):
        curr=self.head
        found=False
        while curr!=None and not found:
            if curr.get_data()==target:
                found=True
            else:
                curr=curr.get_link()
        return found
    def display(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end=" ")
            curr=curr.get_link()
        
linkedlist=LinkedList()
linkedlist.add(43)
print(linkedlist.head.data)
