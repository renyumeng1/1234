class LinkNode:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class LinkList:
    def __init__(self):
        self.head = LinkNode()
        self.head.next = None
    def CreateListF(self,a):#头插法[1,2,3,4]插入后为4321
        for i in range(0,len(a)):
            s = LinkNode(a[i])
            s.next = self.head.next
            self.head.next = s
    def CreateListR(self,a):#尾插法[1,2,3,4]插入后仍为1234
        t = self.head
        for i in range(0,len(a)):
            s = LinkNode(a[i])
            t.next = s
            t = s
        t.next = None
    def geti(self,i):
        p = self.head
        j = -1
        while (j < i and p is not None):
            j+=1
            p = p.next
        return p
    def Add(self,e):
        s = LinkNode(e)
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = s
    def getsize(self):
        p = self.head
        cnt = 0
        while p.next is not None:
            cnt+=1
            p = p.next  
        return cnt
    def __getitem__(self,i):
        assert i>=0
        p = self.geti(i)
        assert p is not None
        return p.data
    def __setitem__(self,i,e):
        assert i>=0
        p = self.geti(i)
        assert p is not None
        p.data = e
    def GetNo(self,e):
        j = 0
        p = self.head.next
        while p is not None and p.data!=e:
            j+=1
            p = p.next
        if p is None:
            return -1
        else:
            return j
    def Insert(self,i,e):
        assert i>=0
        s = LinkNode(e)
        p = self.geti(i-1)
        s.next = p.next
        p.next = s
    def Delete(self,i):
        assert i>=0
        p = self.geti(i-1)
        assert p!=None and p.next is not None
        p.next = p.next.next
    def display(self):
        p = self.head.next
        while p is not None:
            print(p.data,end = ' ')
            p = p.next
        print()
if __name__ == "__main__":
    A = LinkList()
    A.CreateListR([1,2,3,4])
    A.display()
    print(A[1])
    A[2] = 7
    A.display()
        
    