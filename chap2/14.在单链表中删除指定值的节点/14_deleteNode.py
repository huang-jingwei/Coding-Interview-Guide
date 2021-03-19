# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:

        # 要删除的节点是头结点
        if head.val == val:
            nextNode = head.next    # 直接用下一节点覆盖头结点
            head = nextNode
            return head

        # 要删除的节点是除头结点外的其他节点
        preNode = head              # 当前节点的下一节点
        node = head.next            # 当前节点

        # 要删除的节点是中间节点
        while node != None:
            if node.val == val and node.next == None:  # 要删除的节点是尾节点
                preNode.next = None                    # 上一节点的相邻节点直接指向空
                return head

            if node.val == val and node.next != None:  # 要删除的节点是位于链表中间的节点
                nextNode = node.next
                preNode.next = nextNode
                return head

            preNode = node                             # 当前节点不是要删除的节点，节点向下移动
            node = node.next