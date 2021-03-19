# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


# 先序遍历的顺序：中左右
# 中序遍历的顺序：左中右
# 后序遍历的顺序：左右中

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        headNode = self.reConstruct(inorder, postorder)
        return headNode

    def reConstruct(self, inorder, postorder):
        arrayLength = len(postorder)
        if arrayLength == 0:
            return None
        elif arrayLength == 1:
            return TreeNode(postorder[0])

        # 后序遍历的尾节点就是当前二叉树的头结点
        headVal = postorder.pop()
        headNode = TreeNode(headVal)
        # 找出头结点在中序遍历的下标
        headIndex = -1
        for index in range(len(inorder)):
            if inorder[index] == headVal:
                headIndex = index
                break

        # 采用递归方法分别生成该头结点的左子树、右子树
        headNode.left = self.reConstruct(inorder[:headIndex], postorder[:headIndex])
        headNode.right = self.reConstruct(inorder[headIndex + 1:], postorder[headIndex:arrayLength - 1])
        return headNode