class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        length = len(nums)
        if length < 2:
            return 0
        # 基本思路：桶排序+鸽巢定理
        # 参考博客：https://blog.csdn.net/zxzxzx0119/article/details/82889998
        # 参考题解：https://leetcode-cn.com/problems/maximum-gap/solution/mei-xiang-dao-wo-men-zhi-jian-de-zui-da-jian-ju-ji/
        maxValue = max(nums)  # 数组的最大值、最小值
        minValue = min(nums)
        if maxValue == minValue:  # 最大值和最小值相等，证明这个数组是常数组
            return 0

        # step1:求解单个数据桶的数据区间
        # 在 n 个数下，形成的两两相邻区间是 n - 1 个，比如 [2,4,6,8] 这里
        # 例如,有 4 个数，但是只有 3 个区间，[2,4], [4,6], [6,8]
        # 因此，桶长度 = 区间总长度 / 区间总个数 = (max - min) / (nums.length - 1)
        bucketSize = max(1, (maxValue - minValue) // (length - 1))

        # step2:需要几个数据桶
        # 桶个数 = 区间长度 / 桶长度
        # 多加一个桶
        buckNum = (maxValue - minValue) // bucketSize + 1

        # bigBucket[i]：记录第i个数据桶的最大值
        # smallBucket[i]：记录第i个数据桶的最小值
        # isNum[i]：记录第i个数据桶是否拥有数据
        bigBucket = [float("-inf")] * buckNum
        smallBucket = [float("inf")] * buckNum
        isNum = [False] * buckNum

        for index in range(length):
            # step1:判断当前数在哪一个数据桶
            # 已知一个元素，需要定位到桶的时候，一般是 (当前元素 - 最小值) / 桶长度
            bucketIndex = (nums[index] - minValue) // bucketSize
            # step2：更新对应数据桶的信息
            isNum[bucketIndex] = True
            bigBucket[bucketIndex] = max(nums[index], bigBucket[bucketIndex])
            smallBucket[bucketIndex] = min(nums[index], smallBucket[bucketIndex])

        maxGap = float("-inf")  # 记录最大差值
        lastNum = bigBucket[0]

        for index in range(1, buckNum):
            if isNum[index] == True:
                maxGap = max(maxGap, smallBucket[index] - lastNum)
                lastNum = bigBucket[index]
        return maxGap