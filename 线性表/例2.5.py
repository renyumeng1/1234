from ADTlist import SqList
def middle(A,B):#二路归并
    i = j = k = 0
    while  i < A.getsize() and j < B.getsize():
        k+=1
        if A[i] < B[j]:
            if k == A.getsize():
                return A[i]
            i+=1
        else:
            if k ==B.getsize():
                return B[j]    
            j+=1