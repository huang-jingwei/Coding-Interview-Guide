import random


class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = []  # 链表结构，用于储存数据
        self.dataSet = {}  # 辅助哈希表结构，用于判断元素是否重复
        self.nums = 0  # 计数器，记录集合元素个数

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.data.append(val)
        self.nums += 1

        # 记录元素出现的次数
        if val not in self.dataSet:
            self.dataSet[val] = 1
            return True
        else:
            self.dataSet[val] += 1
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if val not in self.dataSet:
            return False
        else:
            # 要删除元素在集合只出现了一次
            if self.dataSet[val] == 1:
                del self.dataSet[val]
                self.data.remove(val)
            # 要删除元素在集合出现了多次
            else:
                self.dataSet[val] -= 1
                # 获取元素在链表中的下标,这种方法只能查找到该元素第一次出现时的下标
                index = self.data.index(val)
                self.data.pop(index)
            self.nums -= 1  # 更新集合中元素的个数
            return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        if self.nums == 0:
            return False
        index = random.randint(0, self.nums - 1)
        return self.data[index]

# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()