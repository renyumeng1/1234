class SqList:
    def __init__(self):
        self.initcapacity = 5
        self.capacity = self.initcapacity
        self.data = self.capacity * [None]
        self.size = 0
    def resize(self,newcapacity):
        assert newcapacity >= 0
        olddata = self.data
        self.data = newcapacity * [None]
        for i in range(self.size):
            self.data[i] = olddata[i]
    def CreateList(self,a):
        for i in range(len(a)):
            if self.size == self.capacity:
                self.resize(2*self.size)
            self.data[self.size] = a[i]
            self.size+=1
    def Add(self,e):
        if self.size == self.capacity:
            self.resize(2*self.size)
        self.data[self.size] = e
        self.size+=1
    def getsize(self):
        return self.size
    def __getitem__(self,i):
        assert 0<=i<self.size
        return self.data[i]
    def __setitem__(self,i,x):
        assert 0<=i<=self.size
        self.data[i] = x
    def GetNo(self,e):
        i = 0
        while i<self.size and self.data[i]!=0:
            i+=1
        if i>self.size:
            return -1
        else:
            return 1
    def Insert(self,i,e):
        assert 0<=i<=self.size
        if self.size == self.capacity:
            self.resize(self.size*2)
        for j in range(self.size,i-1,-1):
            self.data[j] = self.data[j-1]
        self.data[i] = e
        self.size+=1
    def Delete(self,i):
        assert 0<=i<=self.size-1
        for j in range(i,self.size-1):
            self.data[j] = self.data[j+1]
        self.size-=1
        if self.capacity >self.initcapacity and self.size<=self.capacity/4:
            self.resize(self.capacity//2)
    def display(self):
        for i in range(self.size):
            print(self.data[i],end = ' ')
        print()
if __name__ == "__main__":
    Alist = SqList()
    Alist.CreateList([1,2,3,4,5])
    Alist.Add(7)
    Alist.display()
    Alist.Delete(2)
    Alist.display()
    print(Alist.size)
    Alist.Insert(2,9)
    Alist.display()
    
            
    