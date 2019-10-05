import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root

    def levelOrder(self,root):
        #Write your code here
        queue = Queue()
        queue.enqueue(root)
        while not queue.is_empty():
            node = queue.dequeue()
            print(node.data, end=" ")
            if node.left:
                queue.enqueue(node.left)
            if node.right:
                queue.enqueue(node.right)

class Node_:
    def __init__ (self, data):
        self.data = data
        self.link = None


class Queue:
    def __init__ (self):
        self.front = self.back = None

    def is_empty (self):
        return self.front == self.back == None

    def enqueue (self, data):
        node = Node_(data)
        if self.is_empty():
            self.front = node
        else:
            self.back.link = node
        self.back = node

    def dequeue (self):
        data = self.front.data
        next_node = self.front.link
        if next_node:
            self.front = next_node
        else:
            self.front = None
            self.back = None
        return data

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
