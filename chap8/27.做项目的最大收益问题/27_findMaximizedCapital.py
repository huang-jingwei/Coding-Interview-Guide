class Solution:
    def findMaximizedCapital(self, k: int, W: int, Profits: List[int], Capital: List[int]) -> int:
        workDone = []  # 记录已经完成的项目
        canInvest = True  # 判断还能否继续进行投资
        while len(workDone) < k and canInvest == True:
            # 先找出在当前资金下，在未完成的项目中，找出利润最大的项目的编号
            itemIndex = -1
            maxProfit = 0
            for index in range(len(Capital)):
                if (Capital[index] <= W) and (index not in workDone) and (Profits[index] > maxProfit):
                    itemIndex = index
                    maxProfit = Profits[index]

            # 投资利润最大的项目
            if itemIndex != -1:
                workDone.append(itemIndex)
                W += maxProfit
                canInvest = True
            else:
                canInvest = False
        return W