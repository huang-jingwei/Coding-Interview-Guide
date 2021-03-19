import sys   # 修改递归深度
sys.setrecursionlimit(100000)

# 函数功能：逆序数据栈
def inverse(arr):
    if len(arr)==0:
        return []
    stack=[]
    stack.append(arr.pop())
    res=inverse(arr)
    if len(res)>0:
        for val in res:
            stack.append(val)   
    return stack

# step1:获取输入数据
n=int(input())
arr=list(map(int, input().split()))
stack=inverse(arr)

for index in range((len(stack))):
        print(stack[index],end=" ")