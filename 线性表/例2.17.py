from CDLinkList import CDLinkList
def Comb(A,B):
    ta = A.dhead.prior
    tb = B.dhead.prior
    ta.next = B.dhead.next
    B.dhead.prior = ta
    tb.next = ta
    ta.prior = tb
    return A

