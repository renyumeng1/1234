from LinkLIst import LinkList
def Merge2(A,B):
    p = A.head.next
    q = B.head.next
    c = LinkList()
    t = c.head
    while p != None and q != None:
        if p.data < q.data:
            t.next = p
            t = p
            p = p.next
        else:
            t.next = q
            t = q
            q = q.next
        t.next = None
    if p != None:
        t.next = p
    if q != None:
        t.next = q
    return c
    