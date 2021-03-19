class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        # 基本思路：采用二分法划分数组，那么数组就分成两半：
        # 一半数组是有序升序数组，另一半数组是：包含了旋转数组
        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid

            # 情况1：右半部分数组是升序数组,即[mid,right]
            if nums[mid] < nums[right]:
                # 在这段有序数组存在目标数值，那么对该区间进行二分搜索
                # 若该区间不存在目标数值，直接将右边界设置为mid-1，让搜索区间变为左半部分数组
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            # 情况2：左半部分数组是升序数组,即[left,mid]
            else :
                # 在这段有序数组存在目标数值，那么对该区间进行二分搜索
                # 若该区间不存在目标数值，直接将左边界设置为mid+1，让搜索区间变为右半部分数组
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1

        # 目标数在数组中找不到
        return -1