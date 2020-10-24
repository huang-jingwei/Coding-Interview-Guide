import collections

class LRUCache:

    def __init__(self, capacity: int):
        self.data=collections.OrderedDict()  #用有序字典存储数据
        self.size=capacity                   #该数据结构能缓存的最多元素个数


    def get(self, key: int) -> int:
        if key not in self.data:
            return -1
        else:
            self.data.move_to_end(key)
            return self.data[key]

    def put(self, key: int, value: int) -> None:
        self.data[key]=value
        self.data.move_to_end(key)
        if len(self.data)>self.size:
            self.data.popitem(last=False)

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)