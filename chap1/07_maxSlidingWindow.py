class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if len(nums) == 1:
            return nums
        minArray = []        # 存放各个窗口最大值，用于返回
        stack = []           # 辅助数据栈，用来模拟单调栈结构，数值大的元素对应的下标在底部

        for index in range(len(nums)):
            while len(stack) > 0 and nums[index] >= nums[stack[-1]]:
                stack.pop()
            stack.append(index)

            if index - stack[0] >= k:
                del stack[0]
            if index >= k - 1:
                minArray.append(nums[stack[0]])
        return minArray