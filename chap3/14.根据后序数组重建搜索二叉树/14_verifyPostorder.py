# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def verifyPostorder(self, postorder):
        treeLength = len(postorder)
        if treeLength == 0 or treeLength == 1:     # 二叉树没有节点或只有一个节点时，为搜索二叉树
            return True
        return self.reConstruction(postorder,left=0,right=len(postorder)-1)


    #根据后序遍历结果判断二叉树是否是搜索二叉树
    def reConstruction(self,postorder,left,right):
        if left >=right:
            return  True
        #因为后序遍历的顺序为：左右中
        #所以后序遍历的尾节点是头结点
        headVal=postorder[right]

        mid = left-1
        #搜索二叉树节点数值比左儿子节点数值大，比右儿子节点数值小
        #找到当前节点的左子树和右子树的分界点
        while mid+1<=right and postorder[mid+1] <headVal:
            mid  += 1
        #若该二叉树为搜索二叉树，那么分界点的数值(除去最后元素）均大于头结点
        rightIndex=mid
        while rightIndex+1<len(postorder) and postorder[rightIndex+1]>postorder[right]:
            rightIndex +=1
        return  rightIndex==right-1 and self.reConstruction(postorder,mid+1,right-1) and self.reConstruction(postorder,left,mid)