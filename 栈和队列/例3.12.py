MaxSize = 100
class CSqQueue1:
    def __init__(self):
        self.data = [None] * MaxSize
        self.front = 0
        self.count = 0
    def empty(self):
        return self.count == 0
    def push(self,e):
        rear1 = (self.front +self.count) % MaxSize
        assert self.count != MaxSize
        rear1=(rear1+1) % MaxSize
        self.data[rear1] = e
        self.count += 1
    def pop(self):
        assert not self.empty()
        self.count-=1
        self.front = (self.front + 1) % MaxSize
        return self.data[self.front]
    def gethead(self):
        assert not self.empty()
        head = (self.front + 1) % MaxSize
        return self.data[head]
if __name__ == '__main__':
    qu=CSqQueue1()
    qu.push(1)
    qu.push(2)
    qu.push(3)
    qu.push(4)
    print("队头元素: %d" %(qu.gethead()))
    print("出队顺序:",end=' ')
    while not qu.empty():
        print(qu.pop(),end=' ')
    print()

