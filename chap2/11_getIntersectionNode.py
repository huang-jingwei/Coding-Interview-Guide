# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None

        # 计算两个链表的长度
        lengthA = 0    # 初始化两个链表的长度
        lengthB = 0
        nodeA = headA  # 复制两个链表的头节点
        nodeB = headB
        while nodeA != None:
            lengthA += 1
            nodeA = nodeA.next
        while nodeB != None:
            lengthB += 1
            nodeB = nodeB.next
        lengthGap = abs(lengthA - lengthB)

        # 长度较长的链表先进行移动，让两个链表的移动下标距离链表末尾的距离保持一致
        if lengthA >= lengthB:
            while lengthGap > 0:
                headA = headA.next
                lengthGap -= 1

            while headA != None:
                if headA != headB:
                    headA = headA.next
                    headB = headB.next
                else:
                    return headA
            return None
        else:
            while lengthGap > 0:
                headB = headB.next
                lengthGap -= 1

            while headB != None:
                if headA != headB:
                    headA = headA.next
                    headB = headB.next
                else:
                    return headA
            return None