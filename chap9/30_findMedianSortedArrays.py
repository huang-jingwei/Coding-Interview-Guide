class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        array = []
        index1 = 0
        index2 = 0
        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] <= nums2[index2]:
                array.append(nums1[index1])
                index1 = index1 + 1
            elif nums1[index1] > nums2[index2]:
                array.append(nums2[index2])
                index2 = index2 + 1

        # 至少一个列表已经被遍历完了
        if index1 == len(nums1):
            while index2 < len(nums2):
                array.append(nums2[index2])
                index2 = index2 + 1
        elif index2 == len(nums2):
            # index1=index1+1
            while index1 < len(nums1):
                array.append(nums1[index1])
                index1 = index1 + 1

        # 返回中位数
        if len(array) % 2 != 0:
            return array[len(array) // 2]
        elif len(array) % 2 == 0:
            if len(array) == 2:
                return (array[0] + array[1]) / 2
            else:
                midIndex = len(array) // 2
                num = (array[midIndex] + array[midIndex - 1]) / 2
                return num