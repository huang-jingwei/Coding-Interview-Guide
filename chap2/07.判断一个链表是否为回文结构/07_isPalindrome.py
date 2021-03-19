# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head==None or head.next==None:
            return True
        nodeVal=[]          #存放链表节点数值
        while head !=None:
            nodeVal.append(head.val)
            head=head.next
        left=0              #链表的左右边界
        right=len(nodeVal)-1
        while left <right:
            if nodeVal[left] !=nodeVal[right]:
                return False
            left  +=1
            right -=1
        return True