class BST:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def insert(self,data):
        if data<self.data:
            #insert to left
            if self.left is None:
                #check if it is leaf node
                self.left=BST(data)
            else:
                #insert to left subtree
                #recursive call
                self.left.insert(data)
        else:
            #insert to right
            if self.right is None:
                self.right=BST(data)
            else:
                self.right.insert(data)
    def lookup(self,data,parent=None):
        if self.data==data:
            #found
            return self,parent
        elif data<self.data:
            #go left
            if self.data is None:
                return None,None
            else:
                return self.left.lookup(data,self)
        else:
            #go right
            if self.data is None:
                return None,None
            else:
                return self.right.lookup(self,self)
    def delete(self,data):
        #get to be deleted node and its parent
        node,parent=self.lookup(data)
        if node is not None:
            if (node.left is None) and (node.right is None):
                #case 1: 0 child
                if parent.left is node:
                    parent.left=None
                else:
                    parent.right=None
            elif (node.left is None) != (node.right is None):
                #case 2: 1 child
                if node.left:
                    n=node.left
                else:
                    n=node.right
                if parent.left is node:
                    parent.left=n
                else:
                    parent.right=n
                del node
            else:
                #case 3: 2 children
                #replace with inorder successor
                parent=node
                successor=node.right
                while successor.left:
                    successor=successor.left
                node.data=successor.data
                #fix successor's parent node child
                if parent.left==successor:
                    parent.left=successor.right
                else:
                    parent.right=successor.right
        else:
            return "Not found"
    def inorder(self):
        if self.left:
            #if self.lef not none
            self.left.inorder()
        print(self.data,end=" ")
        if self.right:
            #if self.right is not none
            self.right.inorder()
    def preorder(self):
        #access root, then left and right
        print(self.data,end=" ")
        if self.left:
            #if self.lef not none
            self.left.preorder()
        if self.right:
            #if self.right is not none
            self.right.preorder()
    def postorder(self):
        if self.left:
            #if self.lef not none
            self.left.postorder()
        if self.right:
            #if self.right is not none
            self.right.postorder()
        print(self.data,end=" ")
    def reverse(self):
        if self.right:
            #if self.right is not none
            self.right.reverse()
        print(self.data,end=" ")
        if self.left:
            #if self.lef not none
            self.left.reverse()
    def search(self,target):
        if self.data==target:
            #terminating case
            return "Found"
        elif self.left is None and self.right is None:
            #not found
            return "Not found"
        elif target<self.data:
            #search left
            if self.left is None:
                return "Not found"
            else:
                #continue left search
                return self.left.search(target)
        else:
            #search right
            #target>data
            if self.right is None:
                return "Not found"
            else:
                #continue right search
                #recursive case
                return self.right.search(target)
    def minimum(self):
        if self.left is None:
            print("Smallest: ",self.data)
        
            
#main
bst=BST(50)
bst.insert(30)
bst.delete(30)
bst.inorder()
