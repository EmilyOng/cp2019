import sys
class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
class Solution:
    # Write your code here
    def __init__(self):
        self.top=None
        self.front=None
        self.rear=None
    def pushCharacter(self,ch):
        #add ch to the top of the stack
        #ch points to top of the stack
        #ch becomes the new top
        dataobj=Node(ch)
        #created dataobj with data and link
        dataobj.link=self.top
        self.top=dataobj
    def enqueueCharacter(self,ch):
        #queue: add to the rear of the queue
        #node points to rear
        #node becomes the new rear
        dataobj=Node(ch)
        if self.front==self.rear and self.front==None:
            self.front=dataobj
        else:
            self.rear.link=dataobj
        self.rear=dataobj
    def popCharacter(self):
        #filo: remove from top of the stack
        #top becomes next node
        curr=self.top
        self.top=curr.link
        return curr.data
    def dequeueCharacter(self):
        #fifo: remove from front
        dataobj=self.front
        self.front=self.front.link
        return dataobj.data
# read the string s
s=input()
#Create the Solution class object
obj=Solution()   

l=len(s)
# push/enqueue all the characters of string s to stack
for i in range(l):
    obj.pushCharacter(s[i])
    obj.enqueueCharacter(s[i])
    
isPalindrome=True
'''
pop the top character from stack
dequeue the first character from queue
compare both the characters
''' 
for i in range(l // 2):
    if obj.popCharacter()!=obj.dequeueCharacter():
        isPalindrome=False
        break
#finally print whether string s is palindrome or not.
if isPalindrome:
    print("The word, "+s+", is a palindrome.")
else:
    print("The word, "+s+", is not a palindrome.")    
