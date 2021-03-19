#处理输入
#step1:获取两个字符串的长度
stringLength=list(map(int, input().strip().split()))
n=stringLength[0]
m=stringLength[1]
#step2:获取两个字符串
str1=str(input())
str2=str(input())

#主函数入口
if len(str1)!=len(str2):
    print("NO")
    exit()
#若两个字符串互为旋转词，那么两个字符串进行拼接后，必定为回文字符串
string=str1+str2
left=0
right=len(string)-1
while left<right:
    if string[left]==string[right]:
        left +=1
        right -=1
    else:
        print("NO")
        exit()
print("YES")