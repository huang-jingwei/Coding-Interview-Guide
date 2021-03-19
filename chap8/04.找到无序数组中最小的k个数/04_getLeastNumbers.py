import random


class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k == 0:
            return []
        elif k==len(arr):
            return arr
        k = k - 1                # 修改k，让数组下标计数从0开始
        left = 0                 # 数组下标边界
        right = len(arr) - 1
        indexRange = self.partition(arr, left, right)
        while k > indexRange[1] or k < indexRange[0]:
            if k < indexRange[0]:
                right = indexRange[0]
                indexRange = self.partition(arr, left, right)
            else:
                left = indexRange[1]
                indexRange = self.partition(arr, left, right)
        return arr[:k + 1]

    # 荷兰国旗问题的partition过程
    def partition(self, arr, left, right):
        num = arr[random.randint(left, right)]
        less = left - 1
        more = right + 1
        index = left
        while index < more:
            if arr[index] == num:
                index += 1
            elif arr[index] < num:
                less += 1
                arr[index], arr[less] = arr[less], arr[index]
                index += 1
            elif arr[index] > num:
                more -= 1
                arr[index], arr[more] = arr[more], arr[index]
        return [less + 1, more - 1]