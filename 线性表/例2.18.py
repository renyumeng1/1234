from CDLinkList import CDLinkList
def Symm(L):
    flag = True
    p = L.dhead.next
    q = L.dhead.prior
    while flag:
        if p.data != q.data:
            flag = False
        else:
            if p==q or p==q.prior:
                break
            else:
                p = p.next
                q= q.prior
        return flag
