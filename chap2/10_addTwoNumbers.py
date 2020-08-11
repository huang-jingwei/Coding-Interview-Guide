# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 == None:           # 输入的两个链表中有一个为空链表时，直接返回另外的链表
            return l2
        elif l2 == None:
            return l1

        preRemaining = 0         # 前一轮计算扣掉10剩下的数
        countList = ListNode(0)  # 初始化空列表，用来记录两个链表之和
        node = countList
        while l1 and l2:         # 遍历两个链表
            curCount = l1.val + l2.val + preRemaining  # 两个节点数值和上一轮计算三者之和
            node.next = ListNode(curCount % 10)
            preRemaining = curCount // 10
            node = node.next
            l1 = l1.next
            l2 = l2.next

        # 至少有一个链表被遍历结束
        # 再单独将剩余的链表参与计算
        if l1:
            while l1 != None:
                curCount = l1.val + preRemaining
                node.next = ListNode(curCount % 10)
                preRemaining = curCount // 10
                node = node.next
                l1 = l1.next
        else:
            while l2 != None:
                curCount = l2.val + preRemaining
                node.next = ListNode(curCount % 10)
                preRemaining = curCount // 10
                node = node.next
                l2 = l2.next

        # 遍历完两个链表后，再把上一轮计算剩余的数添加到数值之和的链表上
        if preRemaining > 0:
            node.next = ListNode(preRemaining)
        return countList.next