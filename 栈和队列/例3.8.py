from LinkStack import LinkStack
def Reverse(st):
    a = []
    while not st.empty():
        a.append(st.pop())
    for i in range(len(a)):
        st.push(a[i])
    return st
#主程序
st=LinkStack()
print("1,2,3,4依次进栈")
st.push(1)
st.push(2)
st.push(3)
st.push(4)
st.display()
print("st逆置->st1")
print("st1出栈序列: ",end=' ')
st1=Reverse(st)
while not st1.empty():
    print(st1.pop(),end=' ')
print()
