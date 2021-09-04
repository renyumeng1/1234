class DLinkNode:
    def __init__(self,data = None):
        self.data = data
        self.next =None
        self.prior = None
class CDLinkList:
    def __init__(self):
        self.dhead = DLinkNode()
        self.dhead.next = self.dhead
        self.dhead.prior = self.dhead
    def CreateListF(self,a):
        for i in range(0,len(a)):
            s = DLinkNode(a[i])
            s.next = self.dhead.next
            self.dhead.next.prior = s
            self.dhead.next = s
            s.prior = self.dhead
    def CreateListR(self,a):
        t = self.dhead
        for i in range(0,len(a)):
            s = DLinkNode(a[i])
            t.next = s
            s.prior = t
            t = s
        t.next = self.dhead
        self.dhead.prior = t
    def geti(self,i):
        j = -1
        p = self.dhead
        while j<i:
            j+=1
            p = p.next
            if p ==self.dhead:
                break
        return p
    def Add(self,e):
        s = DLinkNode(e)
        p = self.dhead
        while p.next != self.dhead:
            p = p.next
        p.next = s
        s.prior = p
        s.next = self.dhead
        self.dhead.prior = s
    def getsize(self):
        p = self.dhead
        cnt = 0
        while p.next != self.dhead:
            cnt+=1
            p = p.next
        return cnt
    def __getitem__(self,i):
        assert i>=0
        p= self.geti(i)
        assert p!=self.dhead
        return p.data
    def __setitem__(self,i,x):
        assert i >= 0
        p = self.geti(i)
        assert p!=self.dhead
        p.data = x
    def GetNo(self,e):
        j = 0
        p = self.dhead.next
        while p != self.dhead and p.data != e:
            j+=1
            p = p.next
        if p == self.dhead:
            return -1
        else:
            return j
    def Insert(self,i,e):
        assert i >= 0
        s = DLinkNode(e)
        if i==0:
            self.dhead.next = s
            s.prior = self.dhead
            s.next = self.dhead
            self.prior = s
        else:
            p = self.geti(i-1)
            assert p!=self.dhead
            s.next = p.next
            p.next.prior = s
            p.next = s
            s.prior = p
    def Delete(self,i):
        assert i >= 0
        p = self.geti(i)
        assert p !=self.dhead
        p.prior.next = p.next
        p.next.prior = p.prior
    def display(self):
        p = self.dhead.next
        while p!=self.dhead:
            print(p.data,end=' ')
            p = p.next
        print()
if __name__ == '__main__':
    L=CDLinkList()
    a=[1,2,3,4,1]
    L.CreateListF(a)
    print("L: ",end='')
    L.display()
    i=4
    x=10
    print("在序号%d处插入%d" %(i,x))
    L.Insert(i,x)
    print("L: ",end='')
    L.display()
    i=4
    print("删除序号%d处元素" %(i))
    L.Delete(i)
    print("L: ",end='')
    L.display()
    x=20
    print("添加%d元素" %(x))
    L.Add(x)
    print("L: ",end='')
    L.display()
    print("元素1的序号是%d" %(L.GetNo(1)))
    print("L: ",end='')
    L.display()

