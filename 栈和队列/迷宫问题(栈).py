class Box:
    def __init__(self,i1,j1,di1):
        self.i = i1
        self.j = j1
        self.di = di1
from SqStack import SqStack
def mgpath(xi,yi,xe,ye):
    global mg
    st = SqStack()
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    e = Box(xi,yi,-1)
    st.push(e)
    while not st.empty():
        b = st.gettop()
        if b.i == xe and b.j == ye:
            for k in range(len(st.data)):
                print("["+str(st.data[k].i)+','+str(st.data[k].j)+']',end = ' ')
            return True
        find = False
        di = b.di
        while di < 3 and find == False:
            di+=1
            i,j = b.i+dx[di],b.j+dy[di]
            if mg[i][j]==0:
                find = True
        if find:
            b.di = di
            b1 = Box(i,j,-1)
            st.push(b1)
            mg[i][j] = -1
        else:
            mg[b.i][b.j] = 0
            st.pop()
    return False
mg = [[1,1,1,1,1,1],[1,0,1,0,0,1],[1,0,0,1,1,1],[1,0,1,0,0,1],[1,0,0,0,0,1],[1,1,1,1,1,1]]
xi,yi = 1,1
xe,ye = 4,4
print("一条迷宫路径：",end = ' ')
if not mgpath(xi,yi,xe,ye):
    print("不存在迷宫路径")

