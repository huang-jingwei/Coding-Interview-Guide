#处理输入数据
n=int(input())
array=list(map(int, input().strip().split()))

#minIndex[i][0]:代表数值arrayzin中i位置左边最近且值比arr[i]小的位置
#minIndex[i][1]:代表数值arrayzin中i位置右边最近且值比arr[i]小的位置
minIndexArray=[[-1,-1] for i in range(n)]
stack=[]   #辅助单调栈，从小排到大
for i in range(n):
    while len(stack)>0 and array[i]<array[stack[-1]]:
        index=stack.pop()     
        minIndexArray[index][1]=i 
        if len(stack)==0:
           minIndexArray[index][0]=-1
        else:
           minIndexArray[index][0]=stack[-1]
    stack.append(i)
#对单调栈剩余元素进行处理
while len(stack)>0:
     index=stack.pop()     
     minIndexArray[index][1]=-1 
     if len(stack)==0:
        minIndexArray[index][0]=-1
     else:
        minIndexArray[index][0]=stack[-1]

#打印结果
for index in range(n):
    print(minIndexArray[index][0],minIndexArray[index][1])