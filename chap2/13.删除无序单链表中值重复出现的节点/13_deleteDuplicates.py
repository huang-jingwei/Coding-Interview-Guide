class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None or head.next == None:  # 链表为空链表为只有单个元素时，直接返回该链表
            return head
        preNode = head                         # 当前节点的前一节点
        node = head.next                       # 当前节点
        while node != None:                    # 依次访问链表原本元素
            if preNode.val == node.val:        # 当前节点的数值和上一节点不一样时，则需要删除当前节点
                preNode.next = node.next
                node = node.next
            else:                              # 当前节点的数值和上一节点不一样时，则节点向前移动
                preNode = node
                node = node.next
        return head