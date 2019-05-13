class Node:
    
    def __init__(self, data):
        self.data = data
        self.link = None
    

class Queue:
    
    def __init__(self):
        self.front = None
        self.rear = None
    
    def is_empty(self):
        return self.front == self.rear == None
        
    def is_full(self):
        pass # impossible
    
    def enqueue(self, data):
        node = Node(data)
        if self.is_empty():
            self.front = node
        else:
            self.rear.link = node
        self.rear = node
        
    def dequeue(self):    
        if self.is_empty():
            print("Cannot delete from empty queue.")
            return -1
        else:
            data = self.front.data
            if self.front.link == None: # last node
                self.front = None
                self.rear = None                
            else: # not last node
                self.front = self.front.link
            return data

    def peek(self):
        return self.front.data
        
    def display(self):
        if self.is_empty():
            print("Empty queue")
        else:
            curr = self.front
            while curr != None:
                print(curr.data, end=' ')
                curr = curr.link
        print()
