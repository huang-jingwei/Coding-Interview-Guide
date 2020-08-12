# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:  # 链表没有元素或只有一个元素时，返回原链表
            return head

        # 创建一个节点，用来充当哨兵节点
        # 用来判断插入排序是否已经遍历到链表的头部
        sentinel = ListNode(float('-inf'))
        sentinel.next = head

        preNode = head                         # 当前节点的上一节点,该节点前(包括该节点)已经完成排序
        curNode = head.next                    # 当前节点，该节点前的链表元素已经完成排序

        while curNode != None:

            if preNode.val <= curNode.val:     # 节点符合升序遍历，继续向前移动
                preNode = curNode
                curNode = curNode.next
            else:                              # 需要进行插入排序
                preNode.next = curNode.next    # 先断掉原链表
                # 寻找插入位置
                pre1 = sentinel
                pre2 = sentinel.next
                while curNode.val > pre2.val:
                    pre1 = pre2
                    pre2 = pre2.next
                # 进行插入
                pre1.next = curNode
                curNode.next = pre2
                # 节点继续向前移动
                curNode = preNode.next
        return sentinel.next