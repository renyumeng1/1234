MaxSize = 100
class SqQueue:
    def __init__(self):
        self.data = [None] * MaxSize
        self.front = -1
        self.rear = -1
    def empty(self):
        return self.front == self.rear
    def push(self,e):
        assert not self.rear == MaxSize - 1
        self.rear += 1
        self.data[self.rear] = e
    def pop(self):
        assert not self.empty()
        self.front += 1
        return self.data[self.front]
    def gethead(self):
        assert not self.empty()
        return self.data[self.front+1]
    
