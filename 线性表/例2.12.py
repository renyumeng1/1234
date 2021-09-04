from LinkLIst import LinkList
def Commnodes(A,B):
    p = A.head.next
    q = B.head.next
    C = LinkList()
    t = C.head
    while p!=None and q!=None:
        if p.data < q.data:
            p = p.next
        elif q.data < p.data:
            q = q.next
        else:
            s = LinkList(p.data)
            t.next = s
            t = s
            p = p.next
            q = q.next
    t.next = None
    return C