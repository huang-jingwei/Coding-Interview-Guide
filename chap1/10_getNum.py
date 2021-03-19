def getNum(arr, target):
    length = len(arr)  # 数组长度
    maxArr = []  # 两个单调栈结果，分别记录滑动窗口内数组的最大值、最小值对应的下标
    minArr = []

    count = 0  # 满足要求的子数组数量
    left = 0  # 滑动窗口的左\右下标
    right = 0

    while left < length:
        while right < length:
            # 更新滑动窗口的最大值
            while len(maxArr) > 0 and arr[right] >= arr[maxArr[-1]]:
                maxArr.pop()
            maxArr.append(right)

            # 更新滑动窗口的最小值
            while len(minArr) > 0 and arr[right] <= arr[minArr[-1]]:
                minArr.pop()
            minArr.append(right)

            # 判断滑动窗口最大值最小值的差值
            if arr[maxArr[0]] - arr[minArr[0]] > target:
                break
            right += 1
        # 统计子数组数量
        count += (right - left)

        # L所指向的元素将过期，需从更新结构中弹出
        if maxArr[0] == left:
            maxArr.pop(0)
        if minArr[0] == left:
            minArr.pop(0)
        left += 1
    return count


# step1:获取输入数据
length = list(map(int, input().split()))
n, num = length[0], length[1]
arr = list(map(int, input().split()))

# step2：打印结果
res = getNum(arr, num)
print(res)