class LinkNode:
    def __init__(self,data = None):
        self.data = data
        self.next = None
class CLinkList:
    def __init__(self):
        self.head = LinkNode()
        self.head.next = self.head
    def CreateListF(self,a):
        for i in range(0,len(a)):
            s = LinkNode(a[i])
            s.next = self.head.next
            self.head.next = s
    def CreateListR(self,a):
        t = self.head
        for i in range(0,len(a)):
            s = LinkNode(a[i])
            t.next = s
            t = s
        t.next = self.head
    def geti(self,i):
        p = self.head
        j = -1
        while j<i:
            j+=1
            p = p.next
            if p == self.head:
                break
        return p
    def Add(self,e):
        s = LinkNode(e)
        p = self.head
        while p.next != self.head:
            p = p.next
        p.next = s
        s.next = self.head
    def getsize(self):
        p = self.head
        cnt = 0
        while p.next != self.head:
            cnt+=1
            p = p.next
        return cnt
    def __getitem__(self,i):
        assert i>=0
        p = self.geti(i)
        assert p != self.head
        return p.data
    def __setitem__(self,i,x):
        assert i >= 0
        p = self.geti(i)
        assert p != self.head
        p.data = x
    def GetNo(self,e):
        j = 0
        p = self.head.next
        while p!=self.head and p.data != e:
            j+=1
            p = p.next
        if p == self.head:
            return -1
        else:
            return j
    def Insert(self,i,e):
        assert i>=0
        s = LinkNode(e)
        if i==0:
            s.next = self.head.next
            self.head.next = s
        else:
            p = self.geti(i-1)
            assert p != self.head
            s.next = p.next
            p.next = s
    def Delete(self,i):
        assert i>=0
        p = self.geti(i-1)
        assert p.next != self.head
        p.next = p.next.next
    def display(self):
        p = self.head.next
        while p!=self.head:
            print(p.data,end=' ')
            p = p.next
        print()
if __name__ == '__main__':
    L=CLinkList()
    a=[1,2,3,4,1]
    L.CreateListR(a)
    print("L: ",end=''),L.display()
    i=0
    x=10
    print("在序号%d处插入%d" %(i,x))
    L.Insert(i,x)
    print("L: ",end=''),L.display()

    i=5
    print("删除序号%d处元素" %(i))
    L.Delete(i)
    print("L: ",end=''),L.display()

    x=20
    print("添加%d元素" %(x))
    L.Add(x)
    print("L: ",end=''),L.display()

    print("元素1的序号是%d" %(L.GetNo(1)))
    print("L: ",end=''),L.display()
            
        