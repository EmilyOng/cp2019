#Stack; LIFO/FILO
#top=-1, increment/decrement top when adding/removing
class Stack:
    MAX=10
    def __init__(self):
        self.data=[]
        for i in range(self.MAX):
            self.data.append(0)
        #self.data=[0 for i in range(self.MAX)]
        self.top=-1
    def is_empty(self):
        return self.top==-1
    def is_full(self):
        return self.top==self.MAX-1
    def push(self,data):
        if self.is_full():
            print("Cannot insert to full stack.")
            return -1
        else:
            self.top+=1
            self.data[self.top]=data
    def pop(self):
        if self.is_empty():
            print("Cannot delete from an empty stack.")
            return -1
        else:
            data=self.data[self.top]
            self.top-=1
            return data
    def show_top(self):
        #print(s.top)
        data=int(self.data[self.top])
        return data
    def display(self):
        i=self.top
        while i>=0:
            print(self.data[i],end=" ")
            i-=1
        print()
