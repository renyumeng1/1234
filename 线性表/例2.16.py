class Child:
    def __init__(self,nol):
        self.no = nol
        self.next = None
class Joseph:
    def __init__(self,nl,ml):
        self.n = nl
        self.m = ml
        self.first = Child(1)
        t = self.first
        for i in range(2,self.n+1):
            p = Child(i)
            t.next = p
            t = p
        t.next = self.first
    def Jsequence(self):
        for i in range(1,self.n+1):
            p = self.first
            j = 1
            while j < self.m-1:
                j+=1
                p = p.next     
            q = p.next
            print(q.no,end = ' ')
            p.next = q.next
            self.first = p.next
        print()
if __name__ == '__main__':
    n=6
    m=3
    L=Joseph(n,m)
    print("n=%d，m=%d的约瑟夫序列:" %(n,m))
    L.Jsequence()