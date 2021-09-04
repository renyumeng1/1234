from CLinkList import CLinkList
def Count(L,x):
    cnt = 0
    p = L.head
    while p != L.head:
        if p.data == x:
            cnt+=1
        p = p.next
    return cnt