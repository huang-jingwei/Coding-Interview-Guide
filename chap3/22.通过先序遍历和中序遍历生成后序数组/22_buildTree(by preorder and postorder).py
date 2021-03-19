# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 先序遍历的顺序：中左右
# 后序遍历的顺序：左右中

class Solution:
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        arrayLength = len(pre)
        if arrayLength == 0:
            return None
        elif arrayLength == 1:
            return TreeNode(pre[0])
        headNode = self.buildTree(pre, post)
        return headNode

    def buildTree(self, pre, post):
        arrayLength = len(pre)
        if arrayLength == 0:
            return None
        elif arrayLength == 1:
            return TreeNode(pre[0])

        # 先序遍历的头节点就是当前二叉树的头结点
        headVal = pre.pop(0)
        headNode = TreeNode(headVal)

        # 确定左子树的长度
        # 先序遍历中左子树的第一个被访问的节点，在后序遍历中是左子树最后被访问的节点
        leftRootVal = pre[0]
        leftLength = 0

        for index in range(len(post)):
            if post[index] == leftRootVal:
                leftLength = index
                break

        # 采用递归方法分别生成该头结点的左子树、右子树
        headNode.left = self.buildTree(pre[:leftLength + 1], post[:leftLength + 1])
        headNode.right = self.buildTree(pre[leftLength + 1:], post[leftLength + 1:arrayLength - 1])
        return headNode