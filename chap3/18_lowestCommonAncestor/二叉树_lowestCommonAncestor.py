# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root == None:
            return None

        # 递归查询两个节点p q，如果某个节点等于节点p或节点q，则返回该节点的值给父节点
        if root == p or root == q:
            return root

        # 判断当前节点的左右字树是否存在p，q节点
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        # 如果当前节点的左右子树分别包括p和q节点，那么这个节点必然是所求的解
        if left != None and right != None:
            return root

        # 如果当前节点有一个子树的返回值为p或q节点，则返回该值。（告诉父节点有一个节点存在其子树中）
        if left != None:
            return left
        if right != None:
            return right
        return None