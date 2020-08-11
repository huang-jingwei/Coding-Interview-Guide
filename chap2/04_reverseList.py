# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:  # 链表为空链表或只有一个元素时，直接返回该链表
            return head

        nodeData = []                          # 存放原链表的节点信息
        while head != None:
            nodeData.append(ListNode(head.val))
            head = head.next
        left = 0                               # 翻转原链表
        right = len(nodeData) - 1
        while left < right:
            nodeData[left], nodeData[right] = nodeData[right], nodeData[left]
            left += 1
            right -= 1
        for index in range(len(nodeData) - 1):  # 将翻转后的链表重新连接起来
            nodeData[index].next = nodeData[index + 1]
        return nodeData[0]