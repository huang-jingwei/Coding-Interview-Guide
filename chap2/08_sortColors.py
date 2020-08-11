class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #本题采用荷兰国旗问题的思路进行求解
        less=-1                      
        more=len(nums)
        index=0                 #移动下标
        while index<more:
            if nums[index]==1:
                index +=1
            elif nums[index]<1:
                less +=1
                nums[less],nums[index]=nums[index],nums[less]
                index +=1
            elif nums[index]>1:
                more -=1
                nums[more],nums[index]=nums[index],nums[more]
        return nums