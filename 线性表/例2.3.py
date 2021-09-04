from ADTlist import SqList
def deletex1(L,x):
    k = 0
    for i in range(L.getsize()):
        if L[i] != x:
            L[k] = L[i]
            k+=1
    L.size = k
def deletex2(L,x):
    k = 0
    for i in range(L.getsize()):
        if L[i] != x:
            L[i-k] = L[i]
        else:
            k+=1
    L.size -= k
def deletex3(L,x):
    j = 0
    i = -1
    while j < L.getsize():
        if L[j]!=x:
            i+=1
            if i!=j:
                L[i],L[j] = L[j],L[i]
        j+=1
    L.size = i+1
if __name__ == '__main__':
    L = SqList()
    L.CreateList([1,2,2,4,5])
    deletex1(L,2)
    L.display()