from SqStack import SqStack
def isMatch(str):
    st = SqStack()
    i = 0
    while i < len(str):
        e = str[i]
        if e == "(" or e == "[" or e == "{":
            st.push(e)
        else:
            if e == ")":
                if st.empty() or st.gettop() != "(":
                    return False
                st.pop()
            if e == "]":
                if st.empty() or st.gettop() != "[":
                    return False
                st.pop()
            if e == "}":
                if st.empty() or st.gettop() != "{":
                    return False
                st.pop()
        i+=1
    return st.empty()

if __name__ == "__main__":
    #主程序
    print("测试1")
    str="([)]"
    if isMatch(str):
        print(str+"中括号是匹配的")
    else:
        print(str+"中括号不匹配")
    print("测试2")
    str="([])"
    if isMatch(str):
        print(str+"中括号是匹配的")
    else:
        print(str+"中括号不匹配")


