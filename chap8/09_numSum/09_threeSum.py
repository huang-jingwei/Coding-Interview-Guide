class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if nums == None or len(nums) < 3:  # 数组长度小于3，不可能存在3数之和
            return []

        nums.sort()
        answer = []                        # 用来存放所有可行解
        for firstNumIndex in range(len(nums) - 2):
            # 因为对数组进行升序排列，若第一个元素已经大于0，后面的元素必定也大于0
            # 那么他们的和不可能为0
            if nums[firstNumIndex] > 0:
                return answer
            # 对于重复元素：跳过，避免出现重复解
            if firstNumIndex > 0 and nums[firstNumIndex] == nums[firstNumIndex - 1]:
                continue

            left = firstNumIndex + 1
            right = len(nums) - 1
            while left < right:
                if nums[firstNumIndex] + nums[left] + nums[right] == 0:
                    answer.append([nums[firstNumIndex], nums[left], nums[right]])
                    # 对于重复元素：跳过，避免出现重复解
                    while left < right and nums[left] == nums[left + 1]: 
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right = right - 1
                    left = left + 1
                    right = right - 1
                elif nums[firstNumIndex] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[firstNumIndex] + nums[left] + nums[right] > 0:
                    right -= 1
        return answer