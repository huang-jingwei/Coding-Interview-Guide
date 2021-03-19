# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

#中序遍历的打印顺序：左中右
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root==None:
            return []
        inorderNode=[]    #中序遍历的节点数值
        stack=[]          #辅助数据栈

        while len(stack)>0 or root !=None:
            if root!=None:
                stack.append(root)
                root=root.left
            else:
                root=stack.pop()
                inorderNode.append(root.val)
                root=root.right
        return inorderNode