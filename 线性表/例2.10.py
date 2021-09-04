from LinkLIst import LinkList
def Split(L,A,B):
    p = L.head.next#p指向首节点
    t = A.head#t始终指向A的头节点
    while p != None:#遍历p的所有结点
        t.next = p#尾插法
        t = p
        p = p.next #p指向下一个节点
        if p != None:
            q = p.next #将p的下一个节点暂时保存在q中
            p.next = B.head.next #头插法
            B.head.next = p
            p = q #p指向p的下一个节点
    t.next = None