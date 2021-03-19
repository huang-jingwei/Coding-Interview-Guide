import random
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        left = 0          # 数组下标的左右下标
        right = len(nums) - 1
        if right == 0:    # 数组只有一个元素时，直接返回
            return nums[0]
        mid = (0 + len(nums)) // 2
        indexRange = self.partition(nums, left, right)
        while mid < indexRange[0] or indexRange[1] < mid:
            if mid < indexRange[0]:
                right = indexRange[0]
                indexRange = self.partition(nums, left, right)
            elif indexRange[1] < mid:
                left = indexRange[1]
                indexRange = self.partition(nums, left, right)
        return nums[mid]

    # 荷兰国旗问题的partition过程
    def partition(self, nums, left, right):
        num = nums[random.randint(left, right)]
        less = left - 1
        more = right + 1
        index = left
        while index < more:
            if nums[index] == num:
                index += 1
            elif nums[index] < num:
                less += 1
                nums[index], nums[less] = nums[less], nums[index]
                index += 1
            elif nums[index] > num:
                more -= 1
                nums[index], nums[more] = nums[more], nums[index]
        return [less + 1, more - 1]