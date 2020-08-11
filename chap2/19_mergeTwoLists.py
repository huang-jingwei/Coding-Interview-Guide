# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None and l2 == None:     # 判断输入是否为空
            return None
        array = []                        # 初始化数组来存放节点的信息
        while l1 != None and l2 != None:  # 遍历两个链表，采用类似外排的方法对链表的节点进行排序
            if l1.val <= l2.val:
                array.append(l1)
                l1 = l1.next
            else:
                array.append(l2)
                l2 = l2.next

        # 至少有一个列表被遍历完了
        # 把剩下的节点信息放入数组array中
        if l1 == None:
            while l2 != None:
                array.append(l2)
                l2 = l2.next
        else:
            while l1 != None:
                array.append(l1)
                l1 = l1.next

        # 把数组array的节点进行重新连接
        for index in range(len(array) - 1):
            array[index].next = array[index + 1]
        return array[0]