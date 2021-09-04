def Reverse(L):
    p = L.head.next
    L.head.next = None
    while p != None:
        q = p.next
        p.next = L.head.next
        L.head.next = p
        p = q 
        
        