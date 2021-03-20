# 函数功能：按照左右半区的方式重新组合单链表
def relocate(arr, length):
    if length == 0:
        return arr
    left = arr[:(length // 2)]
    right = arr[(length // 2):]

    newArr = []
    leftIndex = 0
    rightIndex = 0
    while leftIndex < len(left) and rightIndex < len(right):
        newArr.append(left[leftIndex])
        newArr.append(right[rightIndex])
        leftIndex += 1
        rightIndex += 1
    if leftIndex < len(left):
        while leftIndex() < len(left):
            newArr.append(left[leftIndex])
            leftIndex += 1
    else:
        while rightIndex < len(right):
            newArr.append(right[rightIndex])
            rightIndex += 1
    return newArr


# step1:获取输入数据
length = int(input())
arr = list(map(int, input().split()))

# step2：对链表进行翻转操作
res = relocate(arr, length)
for index in range(length):
    print(res[index], end=" ")