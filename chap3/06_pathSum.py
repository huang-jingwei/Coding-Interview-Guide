# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import copy


class Solution:
    def __init__(self):
        self.treePath = []        # 用来存放可行解集

    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        if root == None:
            return []
        targetSum = sum
        path = []
        self.findPath(root, targetSum, path)
        return self.treePath

    def findPath(self, root, targetSum, path):
        path.append(root.val)

        # 因为二叉树的路径是根节点到叶子节点
        # 判断当前节点是否是叶子节点
        isLeaf = False
        if root.left == None and root.right == None:
            isLeaf = True

        # 当前路径符合要求时，把当前路径添加到可行解集中
        # 在添加路径时，要采用copy方法复制一次，因为Python是动态列表
        # 否则在下列代码的代码中，path进行弹出元素时，可行解集也会弹出元素
        if isLeaf == True and sum(path) == targetSum:
            self.treePath.append(copy.copy(path))

        # 不是叶子节点时，继续遍历它的儿子节点
        if root.left != None:
            self.findPath(root.left, targetSum, path)
        if root.right != None:
            self.findPath(root.right, targetSum, path)
        # 返回父节点前，在路径上删除当前节点
        path.pop()