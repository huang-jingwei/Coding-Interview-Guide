class Solution:
    def minInsertions(self, s: str) -> int:
        # 基本思路：求出最长回文子序列的长度，再用字符串长度减去它
        # 相当于求最长回文子序列，构不成最长回文子序列的字符就需要插入相同的

        s = list(s)      # 将字符串数据转化为数组形式
        length = len(s)  # 字符串长度

        # step1：求最长回文子序列

        # dp[i][j] 表示s[i..j]中最长回文子序列的长度
        # 若s[i] == s[j]，dp[i][j] = dp[i + 1][j - 1] + 2
        # 否则dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        dp = [[0 for i in range(length)] for j in range(length)]

        for j in range(length):
            dp[j][j] = 1
            for i in range(j - 1, -1, -1):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        # step2:求出最长的回文子序列的长度
        maxLength = dp[0][length - 1]
        return length - maxLength