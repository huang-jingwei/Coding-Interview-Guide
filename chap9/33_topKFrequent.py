class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        item_times = {}  # 统计每个元素出现的次数

        for index in range(len(nums)):
            if nums[index] not in item_times:
                item_times[nums[index]] = 1
            else:
                item_times[nums[index]] += 1
        # step1:记录每个元素出现的次数
        value_array = []  # 用两个列表记录元素及其出现的次数
        times_array = []
        for key, times in item_times.items():
            value_array.append(key)
            times_array.append(times)
        heapSize = len(value_array) - 1  # 元素集合个数(元素集合不包含重复元素),从0开始计数

        # step2：建立大根堆
        for index in range(heapSize):
            self.heapInsert(value_array, times_array, index)
        # step3:不断弹出大根堆堆顶元素
        topK_item = []  # 存放前 K 个高频元素
        while len(topK_item) < k:
            times_array[0], times_array[-1] = times_array[-1], times_array[0]
            value_array[0], value_array[-1] = value_array[-1], value_array[0]
            topK_item.append(value_array.pop())
            times_array.pop()
            heapSize -= 1
            self.heapIfy(value_array, times_array, 0, heapSize)
        return topK_item

    # 函数功能：大根堆结构的堆建立
    def heapInsert(self, value_array, times_array, index):
        parent_index = (index - 1) // 2
        while parent_index >= 0 and times_array[index] > times_array[parent_index]:
            times_array[index], times_array[parent_index] = times_array[parent_index], times_array[index]
            value_array[index], value_array[parent_index] = value_array[parent_index], value_array[index]
            index = parent_index
            parent_index = (index - 1) // 2

    # 函数功能：大根堆结构的堆调整
    def heapIfy(self, value_array, times_array, index, heapSize):
        leftSon = 2 * index + 1  # 左右儿子的下标
        rightSon = 2 * index + 2
        while leftSon <= heapSize:  # 堆调整的前提是该节点至少有左儿子节点
            # 情况1：只存在左儿子节点，那么最多只能进行一次堆调整操作
            if rightSon > heapSize:
                if times_array[index] < times_array[leftSon]:
                    times_array[index], times_array[leftSon] = times_array[leftSon], times_array[index]
                    value_array[index], value_array[leftSon] = value_array[leftSon], value_array[index]
                break
            # 情况2：同时存在左右儿子节点
            else:
                # 找出出现次数最多的儿子节点的下标
                if times_array[leftSon] >= times_array[rightSon]:
                    maxTimesIndex = leftSon
                else:
                    maxTimesIndex = rightSon
                # 若当前节点元素出现次数比出现次数最多的儿子节点还多，那么不需要进行堆调整
                # 反之，则进行交换
                if times_array[index] >= times_array[maxTimesIndex]:
                    break
                else:
                    times_array[index], times_array[maxTimesIndex] = times_array[maxTimesIndex], times_array[index]
                    value_array[index], value_array[maxTimesIndex] = value_array[maxTimesIndex], value_array[index]
                    index = maxTimesIndex
                    leftSon = 2 * index + 1  # 左右儿子的下标
                    rightSon = 2 * index + 2