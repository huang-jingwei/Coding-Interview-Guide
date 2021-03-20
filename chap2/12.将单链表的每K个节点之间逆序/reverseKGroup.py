# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head == None or head.next == None:
            return head

        # step1：储存链表节点
        node = []
        while head != None:
            node.append(head)
            head = head.next
        num = len(node)  # 链表的节点个数

        # step2：进行节点交换
        for i in range(num // k):
            left = i * k
            right = min(left + k - 1, num - 1)
            while left < right:
                node[left], node[right] = node[right], node[left]
                left += 1
                right -= 1

        # step3：重新连接节点
        for index in range(num - 1):
            node[index].next = node[index + 1]
        node[-1].next = None
        return node[0]