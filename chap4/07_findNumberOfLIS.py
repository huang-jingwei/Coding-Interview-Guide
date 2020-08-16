class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if nums == None or len(nums) == 0:
            return 0
        elif len(nums) == 1:
            return 1

        # length[i]：表示以num[i]结尾的最长递增子序列的长度
        # count[i]：表示以num[i]结尾的最长递增子序列出现的次数
        length = [1] * (len(nums))
        count = [1] * (len(nums))

        for index in range(len(nums)):
            for i in range(index):

                if nums[i] < nums[index]:                 # 满足上升序列的要求
                    if length[i] + 1 > length[index]:     # 第一次遇到最长子序列
                        length[index] = length[i] + 1
                        count[index] = count[i]
                    elif length[i] + 1 == length[index]:  # 至少是第二次遇到最长子序列
                        count[index] = count[i] + count[index]
        maxlength = max(length)     # 最长递增子序列的长度
        times = 0                   # 统计最长上升子序列出现的次数
        for i in range(len(length)):
            if length[i] == maxlength:
                times += count[i]
        return times