class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        if len(nums) == 0 or len(nums) == 1:
            return 0

        # 需要进行重新排序的数组的左右边界
        isNeed = False  # 布尔器，判断是否需要重新排序
        left = 0
        right = len(nums) - 1

        for index in range(len(nums)):  # 确定待排序数组的左边界
            if nums[index] >= nums[left]:
                left = index
            else:
                left = index
                isNeed = True
                break

        for index in range(len(nums) - 1, -1, -1):  # 确定待排序数组的右边界
            if nums[index] <= nums[right]:
                right = index
            else:
                right = index
                isNeed = True
                break

        if isNeed == False:
            return 0
        else:
            return right - left + 1