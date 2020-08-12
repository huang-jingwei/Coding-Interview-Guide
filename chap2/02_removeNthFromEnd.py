# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        listLength=0                #计算链表的长度
        node=head
        while node !=None:
            listLength +=1
            node=node.next
        #特殊情形
        #该链表为空链表时或n为0时，不需要进行删除处理
        if listLength==0 or n==0:
            return head
        if n==listLength:           #待删除的节点为头结点
            head=head.next
            return head
        else:                       #待删除的节点为其他结点
            preNode=None
            curNode=head
            nodeIndex=listLength-n  #待删除的节点的顺序索引，从0开始计算
            while nodeIndex>0:
                preNode=curNode
                curNode=curNode.next
                nodeIndex -=1
            #到达要删除的节点
            preNode.next=curNode.next
            return head