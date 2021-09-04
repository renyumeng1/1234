from  ADTlist import SqList
def Merge2(A,B):
    C = SqList()
    i,j = 0
    while i<A.getsize() and j<B.getsize():
        if A[i]<B[j]:
            C.Add(A[i])
            i+=1
        if A[i]>B[j]:
            C.Add(B[j])
            j+=1
    while i <A.getsize():
        C.Add(A[i])
        i+=1
    while j <B.getsize():
        C.Add(B[j])
        j+=1
    return C
        