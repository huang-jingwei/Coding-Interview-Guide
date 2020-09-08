class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        string1=list(text1)   #将字符串数据转化成列表数据
        string2=list(text2)

        m=len(string1)        #获取两个列表的长度
        n=len(string2)

        f=[[0 for i in range(n+1)] for j in range(m+1)]

        for row in range(1,m+1):
            for col in range(1,n+1):
                f[row][col]=max(f[row][col-1],f[row-1][col])
                if string1[row-1]==string2[col-1]:
                    f[row][col]=max(f[row][col],f[row-1][col-1]+1)
        return f[m][n]