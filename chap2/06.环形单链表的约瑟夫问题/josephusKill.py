# 函数功能：单向环形链表的约瑟夫问题
def josephus(arr, length, m):
    while len(arr) > 1:
        # 计算当前轮要进行处决的犯人的下标
        index = m % len(arr)

        # 情况1：待处决的犯人是最后一名犯人
        if index == 0:
            arr = arr[:-1]
        # 情况2：待处决的犯人在链表的中间
        else:
            arr = arr[index:] + arr[:(index - 1)]
    return arr[0]


# step1：处理输入数据
inf = list(map(int, input().split()))
n = inf[0]  # n 表示环形链表的长度
m = inf[1]  # m 表示每次报数到 m 就自杀
human = list(range(1, n + 1))  # 创建human数组，val代表人的编号

# step2:调用函数
res = josephus(human, n, m)
print(res)