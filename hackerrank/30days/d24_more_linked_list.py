class Node:
    def __init__(self,data):
        self.data = data
        self.next = None 
class Solution: 
    def insert(self,head,data):
            p = Node(data)           
            if head==None:
                head=p
            elif head.next==None:
                head.next=p
            else:
                start=head
                while(start.next!=None):
                    start=start.next
                start.next=p
            return head  
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def removeDuplicates(self,head):
        #Write your code here
        all_data = {}
        curr = head
        while curr != None:
            if curr.data in all_data:
                all_data[curr.data] += 1
            else:
                all_data[curr.data] = 1
            curr = curr.next
        duplicates = []
        for data in all_data:
            if all_data[data] > 1:
                for j in range (all_data[data]-1):
                    duplicates.append(data)
        for duplicate in duplicates:
            curr = head
            prev = None
            found = False
            while curr != None:
                if curr.data == duplicate:
                    found = True
                    if prev == None:
                        head = curr.next
                    else:
                        prev.next = curr.next
                prev = curr
                curr = curr.next
                if found:
                    break
        return head
        

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)    
head=mylist.removeDuplicates(head)
mylist.display(head); 
