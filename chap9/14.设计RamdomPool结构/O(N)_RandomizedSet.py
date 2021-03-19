import random
class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums=0       #计数器，记录集合中数据的个数
        self.data=[]      #用链表来存放数据，用于随机返回元素
        self.dataSet={}   #辅助哈希表，用哈于判断元素是否重复

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val not in self.dataSet:
            self.data.append(val)
            self.dataSet[val]=val
            self.nums +=1
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.dataSet:
            self.data.remove(val)
            del self.dataSet[val]
            self.nums -=1
            return True
        else:
            return False


    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if self.nums==0:
            return False
        index=random.randint(0,self.nums-1)
        return self.data[index]

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()