class SqStack:
    def __init__(self):
        self.data = []
    def empty(self):
        if len(self.data) == 0:
            return True
        return False
    def push(self,e):
        self.data.append(e)
    def pop(self):
        assert not self.empty()
        return self.data.pop()
    def gettop(self):
        assert not self.empty()
        return self.data[-1]
