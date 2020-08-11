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
