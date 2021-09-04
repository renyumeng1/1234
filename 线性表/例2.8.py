from LinkLIst import*
def Delmaxnodes(L):
    p = L.head.next
    maxe = p.data
    while p.next != None:
        if p.next.data > maxe:
            maxe = p.next.data
        p = p.next
    pre = L.head#相当于是记录节点
    p = pre.next
    while p != None: #遍历所有节点
        if p.data == maxe:
            pre = p.next #pre指向p的下一个节点（删除p节点）
            p = pre.next #删除p节点后p后移一个指针
        else:
            pre = pre.next #后移一个指针
            p = pre.next
            
            