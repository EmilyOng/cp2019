class Node:
    def __init__(self,data):
        self.data=data
        self.link=None
class Queue:
    MAX=10
    def __init__(self):
        self.front=None
        self.rear=None
    def is_empty(self):
        return self.front==self.rear
    def is_full(self):
        pass
    def enqueue(self,data):
        if self.is_full():
            print("Cannot insert to full queue.")
            return -1
        else:
            if self.front==None:
                self.front=self.rear
            node=Node(data)
            node.link=self.rear
            self.rear=node
    def dequeue(self):
        if self.is_empty():
            print("Cannot delete from empty queue.")
            return -1
        else:
            pointer=self.rear
            while pointer!=None:
                if pointer.link==self.front:
                    #delete pointer.data
                    pointer.link=None
                    self.front=pointer.data
                pointer=pointer.link
    def peek(self):
        print(self.front.data)
    def display(self):
        pointer=self.rear
        datas=[]
        while pointer!=None:
            datas.append(pointer.data)
            pointer=pointer.link
        datas.reverse()
        for i in datas:
            print(i,end=" ")
        print()
q=Queue()
