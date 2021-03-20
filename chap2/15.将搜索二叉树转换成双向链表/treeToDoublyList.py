"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        # step:二叉树的中序遍历
        arr = self.inorderPrint(root)
        length = len(arr)
        if length == 0:
            return root

        # step2：重新定义node节点的right节点
        for index in range(length - 1):
            arr[index].right = arr[index + 1]
        arr[-1].right = arr[0]

        # step3：重新定义node节点的left节点
        for index in range(length - 1, 0, -1):
            arr[index].left = arr[index - 1]
        arr[0].left = arr[-1]

        return arr[0]

    # 函数功能：二叉树的中序遍历
    def inorderPrint(self, root):
        if root == None:
            return []
        arr = []
        left = self.inorderPrint(root.left)
        if len(left) > 0:
            for node in left:
                arr.append(node)

        arr.append(root)
        right = self.inorderPrint(root.right)
        if len(right) > 0:
            for node in right:
                arr.append(node)
        return arr