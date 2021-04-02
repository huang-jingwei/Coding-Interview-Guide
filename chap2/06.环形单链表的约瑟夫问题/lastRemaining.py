class Solution:
    def lastRemaining(self, n: int, m: int) -> int:
        if n < 1 or m < 1:
            return -1

        number = list(range(n))  # 目标列表
        begin = 0                # 下标与index=begin之间的距离为m的数即为所要删除的数值
        while len(number) > 1:
            delIndex = (begin + m - 1) % len(number)
            del number[delIndex]
            begin = delIndex
        return number[0]