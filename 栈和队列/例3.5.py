from SqStack import SqStack
def isPalindrome(str):
    st = SqStack()
    i = 0
    n = len(str)
    while i < n//2:
        st.push(str[i])
        i+=1
    if n%2 == 1:
        i+=1
    while i < n:
        if st.pop() != str[i]:
            return False
    return True



print("测试1")
str="abcba"
if isPalindrome(str):
    print(str+"是回文")
else:
    print(str+"不是回文")
print("测试2")
str="1221"
if isPalindrome(str):
    print(str+"是回文")
else:
    print(str+"不是回文")

