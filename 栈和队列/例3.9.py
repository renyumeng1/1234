from LinkStack import LinkStack
def isSerial(a,b,n):
    st = LinkStack()
    i,j = 0,0
    while i<n:
        st.push(a[i])
        i+=1
        while not st.empty() and st.gettop() == b[j]:
            st.pop()
            j+=1
    return st.empty()
#主程序
n=4
a=[1,2,3,4]
print("测试1")
b=[1,3,2,4]
if isSerial(a,b,n):
    print(b,"是合法的出栈序列")
else:
    print(b,"不是合法的出栈序列")
print("测试2")
c=[4,3,1,2]
if isSerial(a,c,n):
    print(c,"是合法的出栈序列")
else:
    print(c,"不是合法的出栈序列")
