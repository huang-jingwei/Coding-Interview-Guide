# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# 根据完全二叉树的定义
# 情形1、完全二叉树的层序遍历中不能出现None节点
# 情形2、若一个节点只存在右儿子节点，则必然存在左儿子节点
# 情形3、若一个节点只存在左儿子节点，那么该节点之后的全部节点必须为叶子节点
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        if root == None:  # 输入二叉树为空二叉树
            return True

        queue = []        # 层序遍历中的辅助队列结构
        nodeData = []     # 层序遍历中的节点
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node != None:
                queue.append(node.left)
                queue.append(node.right)
            nodeData.append(node)

        # 去除层序遍历尾部多余的None节点
        while len(nodeData) > 0 and nodeData[-1] == None:
            nodeData.pop()

        isOnlyLeftSon = False  # 用来记录是否存在某个节点只有左儿子节点
        for index in range(len(nodeData)):
            # 情形1、完全二叉树的层序遍历中不能出现None节点
            if nodeData[index] == None:
                return False
            # 情形2、若一个节点只存在右儿子节点，则必然存在左儿子节点
            elif nodeData[index].left == None and nodeData[index].right != None:
                return False
            # 情形3、若一个节点只存在左儿子节点，那么该节点之后的全部节点必须为叶子节点
            # 找出第一个只存在左儿子节点的节点
            elif nodeData[index].left != None and nodeData[index].right == None:
                isOnlyLeftSon = True
                break
        if isOnlyLeftSon == True:  # 存在节点node只存在左儿子节点
            # 若一个节点只存在左儿子节点，那么该节点之后的全部节点必须为叶子节点
            for i in range(index + 1, len(nodeData)):
                if nodeData[i] == None:
                    return False
                elif nodeData[i].left != None and nodeData[i].right != None:
                    return False
        return True