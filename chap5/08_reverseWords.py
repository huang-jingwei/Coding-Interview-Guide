class Solution:
    def reverseWords(self, s: str) -> str:
        if s == None:
            return s

        stringList = s.strip().split()  # 去掉字符串的头尾空格，已经字符串间以空格划分
        leftIndex = 0
        rightIndex = len(stringList) - 1
        while leftIndex < rightIndex:
            stringList[leftIndex], stringList[rightIndex] = stringList[rightIndex], stringList[leftIndex]
            leftIndex = leftIndex + 1
            rightIndex = rightIndex - 1
        string = ""
        for index in range(len(stringList)):
            if index != len(stringList) - 1:
                string = string + stringList[index] + " "
            else:
                string = string + stringList[index]
        return string