# 主函数入口
def wayCount(n, m, k, p):
    # 输入参数是无效时
    if n < 2 or k < 1 or m < 1 or m > n or p < 1 or p > n:
        return 0
    # count[j][i]:代表了用j步走到i位置的方法个数
    # 初始化时，多增加了j=0行来进行初始位置的初始化
    count = [[0 for i in range(n)] for j in range(k + 1)]
    count[0][p - 1] = 1
    value = 10 ** 9 + 7  # 用于求模

    for rest in range(1, k + 1):
        for index in range(n):
            if index == 0:
                count[rest][index] = count[rest - 1][index + 1]
            elif index == n - 1:
                count[rest][index] = count[rest - 1][index - 1]
            else:
                count[rest][index] = count[rest - 1][index - 1] + count[rest - 1][index + 1]
                count[rest][index] = count[rest][index] % value
    ways = count[-1][m - 1]
    return ways


if __name__ == "__main__":
    # 获取输入
    inputArray = list(map(int, input().split()))
    n = inputArray[0]
    m = inputArray[1]
    k = inputArray[2]
    p = inputArray[3]
    # 问题解决函数
    count = wayCount(n, m, k, p)
    print(count)