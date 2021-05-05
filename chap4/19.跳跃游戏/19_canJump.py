class Solution:
    def canJump(self, nums: List[int]) -> bool:
        length=len(nums)  # 数组长度
        reach=nums[0]     # 能到达的最远距离
        for index in range(length):
            reach=max(reach,nums[index]+index)
            if nums[index]<reach: # 无法跳跃到当前位置
                return False
            if reach>=length-1:   # 已到达数组的右边界
                return True
        return False