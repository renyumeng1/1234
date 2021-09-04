from DLinkList import DLinkList
def del(L,x):
    p = L.dhead.next
    while p.next != None and p.data != x:
        p = p.next
    if p!=None:
        p.prior.next = p.next
        if p.next != None:
            p.next.prior = p.prior
            