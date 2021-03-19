length=int(input()) #字符串的长度
str=input()         #目标字符串
res=-1
for index in range(length):
    item=input()
    if item==str:
        res=index
        break
print(res)  