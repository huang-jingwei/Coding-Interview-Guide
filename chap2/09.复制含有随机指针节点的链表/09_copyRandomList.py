# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head == None:          # 输入节点是空节点,z直接返回空节点
            return None

        # 将nodeData= {None:None}进行这样子的初始化，其实就是先将最后的空节点压入
        # 否则在最后的重构链表节点时候，找不到空节点进行连接
        nodeData = {None: None}  # 用字典结构存放节点信息
        node = head
        while node:
            nodeData[node] = Node(node.val)
            node = node.next

        node = head             # 连接节点
        while node:
            nodeData[node].next = nodeData[node.next]
            nodeData[node].random = nodeData[node.random]
            node = node.next
        return nodeData[head]