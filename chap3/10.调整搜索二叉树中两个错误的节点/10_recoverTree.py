# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # step1:原二叉树的中序遍历
        arr = self.inorderPrint(root)
        num = len(arr)  # 二叉树节点个数
        val = []
        for index in range(num):
            if arr[index] != None:
                val.append(arr[index].val)
        val = sorted(val)

        # step2：搜索二叉树的中序遍历是升序数组
        # 基于这个特性，修改二叉树中错误的节点
        i = 0
        for index in range(num):
            if arr[index] != None:
                arr[index].val = val[i]
                i += 1

    # 函数功能：搜索二叉树的中序遍历
    # 注意,搜索二叉树的中序遍历是升序数组
    def inorderPrint(self, root):
        if root == None:
            return [None]
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