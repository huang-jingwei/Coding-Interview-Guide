# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    # 层次序列的序列化
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if root == None:      # 头节点为空时，那么直接返回"[]"
            return "[]"
        nodeData = []        # 用来存放二叉树节点层次遍历的信息
        queue = []           # 层序遍历的队列
        queue.append(root)
        while len(queue) > 0:
            node = queue.pop(0)
            if node == None:
                nodeData.append("null")
            else:
                nodeData.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
        # 删除尾部多余的"null"
        # 叶子节点的左右儿子节点均为None类型，采用上述方法都会将其压入节点列表中
        # 所以要将其删除
        while len(nodeData) > 0 and nodeData[-1] == "null":
            nodeData.pop()
        res = ""
        for i in nodeData:
            res += "," + i
        return res[1:]

    # 层次遍历的反序列化
    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

        if data == "" or data == "[]":  # 输入为空时，直接返回空节点
            return None

        # 理论上要去掉输入字符串头尾两端的"["和"]"
        # 但是在测试的时候，发现传进来的数据没有"["和"]"
        nodeVal = data.split(",")         # 将字符串数据用","将其分割，转化成列表类型数据
        root = TreeNode(int(nodeVal[0]))  # 头结点

        queue = []                        # 层序遍历的队列结构
        queue.append(root)
        index = 1

        # 链接节点信息
        while len(queue) > 0:
            node = queue.pop(0)

            # 判断该节点是否存在左儿子节点
            if index < len(nodeVal) and nodeVal[index] != "null":
                node.left = TreeNode(int(nodeVal[index]))
                queue.append(node.left)
            index += 1

            if index < len(nodeVal) and nodeVal[index] != "null":
                node.right = TreeNode(int(nodeVal[index]))
                queue.append(node.right)
            index += 1
        return root