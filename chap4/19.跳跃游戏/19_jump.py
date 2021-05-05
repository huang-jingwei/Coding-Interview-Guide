class Solution:
    def jump(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0 or length == 1:  # 数组没有元素或者只有一个元素时，不需要跳跃
            return 0
        step = 0                        # 跳跃步数
        reach = 0                       # 当前步数下能到达的最远距离
        nextReach = float("-inf")       # 下一步能到达的最远距离

        for index in range(length):
            nextReach = max(nextReach, nums[index] + index)
            if nextReach >= length - 1:  # 对数组的边界进行约束
                return step + 1
            if index == reach:
                step += 1
                reach = nextReach
        return step