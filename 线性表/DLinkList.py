class DLinkNode:
    def __init__(self,data = None):
        self.data = data
        self.next = None
        self.prior = None
class DLinkList:
    def __init__(self):
        self.dhead = DLinkNode()
        self.dhead.next = None
        self.dhead.prior = None
    def CreateListF(self,a):
        for i in range(0,len(a)):
            s = DLinkNode(a[i])
            s.next = self.dhead.next
            if self.dhead.next is not None:
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
        t.next = None
    def geti(self,i):
        p = self.dhead
        j = -1
        while (j < i and p is not None):
            j+=1
            p = p.next
        return p
    def Add(self,e):
        s = DLinkNode(e)
        p = self.dhead
        while p.next is not None:
            p = p.next
        p.next = s
    def getsize(self):
        p = self.dhead
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
        p = self.dhead.next
        while p is not None and p.data!=e:
            j+=1
            p = p.next
        if p is None:
            return -1
        else:
            return j
    def Insert(self,i,e):
        assert i >= 0 
        s = DLinkNode(e)
        p = self.geti(i-1)
        s.next = p.next
        if p.next != None:
            p.next.prior = s
        p.next = s
        s.prior = p
    def Delete(self,i):
        assert i>=0
        p = self.geti(i)
        assert p is not None
        p.prior.next = p.next
        if p.next != None:
            p.next.prior = p.prior
    def display(self):
        p = self.dhead.next
        while p !=None:
            print(p.data,end=' ')
            p = p.next
        print()
            
if __name__ == "__main__":
    L = DLinkList()
    L.CreateListR([1,2,3,4,5])
    print(L[1])
    L.Add(6)
    L.display()
    