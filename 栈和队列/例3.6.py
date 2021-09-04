class STACK:
    def __init__(self):
        self.data = []
        self.__mindata = []
    def __minempty(self):
        return len(self.__mindata) == 0
    def __minpush(self,e):
        self.__mindata.append(e)
    def __minpop(self):
        assert not self.__minempty()
        return self.__mindata.pop()
    def __mingettop(self):
        assert not self.__minempty()
        return self.__mindata[-1]
    def empty(self):
        return len(self.data) == 0
    def push(self,x):
        if self.empty() or x <=self.__mingettop():
            self.__mindata.append(x)
        self.data.append(x)
    def pop(self):
        assert not self.empty()
        x = self.data.pop()
        if x == self.__mingettop():
            self.__minpop()
        return x
    def gettop(self):
        assert not self.empty()
        return self.data[-1]
    def Getmin(self):
        assert not self.empty()
        return self.__mindata[-1]

#主程序
st=STACK()
print("\n  元素5,6,3,7依次进栈")
st.push(5)
st.push(6)
st.push(3)
st.push(7)
print("  求最小元素并出栈")
while not st.empty():
    print("    最小元素:%d" %(st.Getmin()))
    print("    出栈元素:%d" %(st.pop()))
print()
