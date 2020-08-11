#本题目有两个对应的leetcode题目

#下面这段代码对应零钱兑换
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        elif amount == 0:
            return 0

        count = [float("inf") for i in range(amount + 1)]
        count[0] = 0       # 初始化边界条件

        for money in range(1, len(count)):
            for coin in coins:
                if money >= coin:
                    count[money] = min(count[money], count[money - coin] + 1)
        amountCount = count[-1]

        if amountCount == float("inf"):
            return -1
        else:
            return amountCount


#下面这段代码对应零钱兑换 II
#这个代码是没问题的，但是leetcode测试时遇到长列表会超出时间限制，以后再来优化了
class Solution2:
    def change(self, amount: int, coins: List[int]) -> int:
        # 总面额为0时,存在一种方法进行找零，那就是不找零
        if amount == 0:  # 这个初始化条件是leetcode反反复复测试失败得到的....诡异
            return 1

        # waysCount[i][j]:代表用前i类硬币拼凑出总面额为j的硬币的方案总数
        # waysCount[i][j]=-1：表示用前i类硬币无法拼凑出总面额为j的硬币
        # 在初始化时，额外加入单枚面额为0的硬币
        waysCount = [[-1 for i in range(amount + 1)] for j in range(len(coins) + 1)]
        waysCount[0][0] = 1  # 用面额为0的硬币拼出总面额为0,只有一种

        for coinIndex in range(1, len(coins) + 1):

            # 因为在初始化时，额外加入单枚面额为0的硬币
            # 在waysCount列表中的硬币种类下标coinIndex对应着列表coins中硬币种类下标coinIndex-1
            curCoin = coins[coinIndex - 1]  # 单枚当前类别硬币的面额

            for count in range(amount + 1):

                k = count // curCoin  # 当前的总面额最多可以包含多少枚该类别的硬币
                way = 0  # 计数器，统计当前类别硬币和之前类别的硬币有多少种组合方法拼出该总额的硬币
                for j in range(k + 1):
                    if count - j * curCoin >= 0 and waysCount[coinIndex - 1][count - j * curCoin] != -1:
                        way += waysCount[coinIndex - 1][count - j * curCoin]
                if way != 0:
                    waysCount[coinIndex][count] = way

        if waysCount[-1][-1] == -1:
            return 0
        else:
            return waysCount[-1][-1]