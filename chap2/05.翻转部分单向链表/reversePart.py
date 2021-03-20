# 函数功能：翻转链表
def reversePart(arr,length,left,right):
    while left<right:
        arr[left-1],arr[right-1]=arr[right-1],arr[left-1]
        left +=1
        right -=1
    return arr


# step1：获取输入数据
n=int(input())
val=list(map(int, input().split()))
indexRange=list(map(int, input().split()))
left=indexRange[0]
right=indexRange[1]


# step2：对链表指定区间的数值进行翻转
arr=reversePart(val, n, left, right)

# step3:打印链表
for index in range(n):
    print(arr[index],end=" ")