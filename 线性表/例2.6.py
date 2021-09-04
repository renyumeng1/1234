from LinkLIst import LinkList
def Middle1(L):
    j = 1
    p = L.head.next
    n = L.getsize()
    while j<=(n-1)//2:
        j+=1
        p = p.next
    return p.data
L = LinkList()
L.CreateListR([1,2,3,4,5])
print(Middle1(L))
def Middle2(L):
    slow = L.head.next
    fast = L.head.next
    while fast is  not None and fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data
print(Middle2(L))