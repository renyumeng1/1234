from LinkLIst import LinkList
def Maxcount1(L):
    p = L.head.next
    cnt = 1
    maxe = p.data
    while p.next != None:
        if p.next.data > maxe:
            maxe = p.next.data
            cnt = 1
        elif p.next.data==maxe:
            cnt+=1
        p = p.next
    return cnt
def Maxcount2(L):#有错
    p = L.head.next
    cnt = 0
    maxe = p.data
    while p.next != None:
        if p.data > maxe:
            maxe = p.data
            cnt = 1
        elif p.data==maxe:
            cnt += 1
        p = p.next
    return cnt
L = LinkList()
L.CreateListR([1,1,2,2,3,3,4,4,5,5,5,5])
print(Maxcount1(L))
print(Maxcount2(L))