class Queue:
    MAX=10
    def __init__(self):
        self.queue=[]
        for i in range(self.MAX):
            self.queue.append(0)
        self.front=0 #location to delete
        self.rear=0 #location to insert
    def is_empty(self):
        return self.front==self.rear
    def is_full(self):
        return self.size()==self.MAX-1
    def size(self):
        if self.is_empty():
            return 0
        elif self.front<self.rear:
            return self.rear-self.front
        else:
            return self.rear+self.MAX-self.front
    def enqueue(self,data):
        if self.is_full():
            print("Cannot insert to full queue.")
            return -1
        else:
            self.queue[self.rear]=data
            self.rear=(self.rear+1)%self.MAX
    def dequeue(self):
        if self.is_empty():
            print("Cannot delete from empty queue.")
            return -1
        else:
            data=self.queue[self.front]
            self.front=(self.front+1)%self.MAX
            return data
    def peek(self):
        return self.queue[self.front]
    def display(self):
        if self.is_empty():
            print("Empty queue")
        else:
            if self.front<self.rear:
                for i in range(self.front,self.rear):
                    print(self.queue[i],end=" ")
                print()
            else:
                #wrap around
                for i in range(self.front,self.MAX):
                    print(self.queue[i],end=" ")
                for i in range(0,self.rear):
                    print(self.queue[i],end=" ")
                print()
