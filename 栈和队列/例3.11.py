from CSqQueue import CSqQueue
def pushk(qu,k,e):
    n = qu.size()
    if k < 1 or k > n+1:
        return False
    if k <= n:
        for i in range(1,n+1):
            if i == k:
                qu.push(e)
            x = qu.pop()
            qu.push(x)
    else:
        qu.push(e)
    return True
def popk(qu,k):
    n = qu.size()
    assert k>=1 and k<=n
    for i in range(1,n+1):
        x = qu.pop()
        if i != k:
            qu.push(x)
        else:
            e = x
    return e
#主程序
qu=CSqQueue()
qu.push(1)
qu.push(2)
qu.push(3)
qu.push(4)
print("元素个数=%d" %(qu.size()))
pushk(qu,1,5)
popk(qu,2)
while not qu.empty():
    print(qu.pop(),end=' ')
print()
