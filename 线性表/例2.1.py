from ADTlist import SqList
lst = SqList()
lst.CreateList([1,2,3,4,5])
i = 0
j = lst.getsize()-1
while i<j:
    lst.data[i],lst.data[j] = lst.data[j],lst.data[i]
    i+=1
    j-=1
lst.display()