MaxSize = 100
class CSqQueue:
    def __init__(self):
        self.data = [None] * MaxSize
        self.front = 0
        self.rear = 0
    def empty(self):
        return self.front == self.rear
    def push(self,e):
        assert (self.front + 1) % MaxSize != self.front
        self.rear = (self.rear+1)%MaxSize
        self.data[self.rear] = e
    def pop(self):
        assert not self.empty()
        self.front = (self.front + 1) % MaxSize
        return self.data[self.front]
    def gethead(self):
        assert not self.empty()
        head = (self.front + 1) % MaxSize
        return self.data[head]
    def size(self):
        return ((self.rear-self.front + MaxSize) % MaxSize)
