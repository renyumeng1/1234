from ADTlist import SqList
def deletek(L,i,k):
    assert i>=0 and k>=1 and i+k<=L.getsize()
    for j in range(i+k,L.getsize()):
        L[j-k] = L[j]
    L.size-=k
if __name__ == '__main__':
    L = SqList()
    L.CreateList([1,2,3,4,5])
    deletek(L,2,2)
    L.display()