class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return 1

        data = {}  # 储存数组中所有正数

        for index in range(length):
            item = nums[index]
            if item > 0:
                # 存放数组的正数，key：元素数值，value：index
                if item not in data:
                    data[item] = [index]
                else:
                    data[item].append(index)

        postiveNum = 1  # 按照顺序，依次应该出现的正数

        for index in range(length):
            if nums[index] > 0:
                # 情况1：该正数在数组中不存在
                if postiveNum not in data:
                    return postiveNum

                # 情况2：该正数存在，但是出现次序是在当前索引的后面
                exactIndexRange = data[nums[index]]
                if index not in exactIndexRange:
                    return postiveNum

                postiveNum += 1
        return postiveNum