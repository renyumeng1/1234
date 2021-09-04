class SqStack:
    def __init__(self):
        self.data = []
    def empty(self):
        if len(self.data) == 0:
            return True
        return False
    def push(self,e):
        self.data.append(e)
    def pop(self):
        assert not self.empty()
        return self.data.pop()
    def gettop(self):
        assert not self.empty()
        return self.data[-1]
class ExpressClass:
    def __init__(self,str):
        self.exp = str
        self.postexp = []
    def getpostexp(self):
        return self.postexp
    def Trans(self):
        opor = SqStack()
        i = 0
        while i < len(self.exp):
            ch = self.exp[i]
            if ch =='(':
                opor.push(ch)
            elif ch == ')':
                while not opor.empty() and opor.gettop() != '(':
                    e = opor.pop()
                    self.postexp.append(e)
                opor.pop()
            elif ch =='+' or ch =='-':
                while not opor.empty() and opor.gettop() != '(':
                    e = opor.pop()
                    self.postexp.append(e)
                opor.push(ch)
            elif ch =='*' or ch == '/':
                while not opor.empty():
                    e = opor.gettop()
                    if e != '(' and (e == "*" or e==('/')):
                        e = opor.pop()
                        self.postexp.append(e)
                    else:
                        break
                opor.push(ch)
            else:
                d = ''
                while ch>='0' and ch<='9':
                    d+=ch
                    i+=1
                    if i < len(self.exp):
                        ch  = self.exp[i]
                    else:
                        break
                i-=1
                self.postexp.append(int(d))
            i+=1
        while not opor.empty():
            e = opor.pop()
            self.postexp.append(e)
    def getValue(self):
        opand = SqStack()
        i = 0
        while i < len(self.postexp):
            opv = self.postexp[i]
            if opv =="+":
                a = opand.pop()
                b = opand.pop()
                c = b + a
                opand.push(c)
            elif opv == "-":
                a = opand.pop()
                b = opand.pop()
                c = b-a
                opand.push(c)
            elif opv == "*":
                a = opand.pop()
                b = opand.pop()
                c = b*a
                opand.push(c)
            elif opv == "/":
                a = opand.pop()
                b = opand.pop()
                assert a != 0
                c = b/a
                opand.push(c)
            else:
                opand.push(opv)
            i+=1
        return opand.gettop()
if __name__ == "__main__":
    str = '(56-20)/(4+2)'
    print("中缀表达式:"+str)
    obj = ExpressClass(str)
    obj.Trans()
    print("后缀表达式:",obj.getpostexp())
    print("求值结果：  %g" %(obj.getValue()))


