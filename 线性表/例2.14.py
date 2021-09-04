from DLinkList import DLinkList
def Swap(L,x):
    p = L.dhead.next
    q = None
    while p!=None:#找到最后一个为x的节点
        if p.data == x:
            q = p
        p = p.next
    if q == None or L.dhead.next == q:
        return
    else:
        pre = q.prior
        pre.next = q.next
        if q.next != None:
            q.next.prior = pre
        pre.prior.next = q
        q.prior =pre.prior
        q.next = pre
        pre.prior = q   
if __name__ == "__main__":
    L=DLinkList()
    a=[1,5,6,3,5,6]
    L.CreateListR(a)
    print("L: ",end=''),L.display()
    x=6
    print("x=",x)
    print("交换")
    Swap(L,x)
    print("L: ",end=''),L.display()
    
        