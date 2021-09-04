class LinkNode:
    def __init__(self,data=None):
        self.data = data
        self.next = None
class LinkStack:
    def __init__(self):
        self.head = LinkNode()
        self.head.next = None
    def empty(self):
        if self.head.next is None:
            return True
        return False
    def push(self,e):
        p = LinkNode(e)
        p.next = self.head.next
        self.head.next = p
    def pop(self):
        assert self.head.next is not None
        p = self.head.next
        self.head.next = p.next
        return p.data
    def gettop(self):
        assert self.head.next is not None
        return self.head.next.data
    def display(self):
        p = self.head.next
        while p is not None:
            print(p.data,end = ' ')
            p = p.next
        print()

if __name__ == '__main__':
    st=LinkStack()
    st.push(1)
    st.push(2)
    st.push(3)
    st.push(4)
    st.display()
    print("出栈顺序:",end=' ')
    while not st.empty():
        print(st.pop(),end=' ')
    print()


