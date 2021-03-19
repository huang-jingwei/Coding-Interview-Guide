class Solution:
    def findMin(self, nums: List[int]) -> int:

        #基本思路：
        # 情况1：若该升序列表没有被旋转过，那么最小值元素就是第一个元素
        # 情况2：若该升序列表有被旋转过，那么最小值元素就是交接点

        isTravl=False     #布尔器，用来记录该数组是否被旋转过
        minValue=nums[0]  #最小值元素


        for index in range(len(nums)-1):
            if nums[index]>nums[index+1]:
                isTravl=True
                minValue=nums[index+1]
                break
        return minValue