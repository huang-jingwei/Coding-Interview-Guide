class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:      # 只有一个元素
            return nums[0]

        maxSubArraySum = [0] * len(nums)
        for index in range(len(maxSubArraySum)):
            if index == 0:
                maxSubArraySum[index] = nums[index]
            elif index > 0:
                if maxSubArraySum[index - 1] >= 0:
                    maxSubArraySum[index] = maxSubArraySum[index - 1] + nums[index]
                else:
                    maxSubArraySum[index] = nums[index]
        return max(maxSubArraySum)