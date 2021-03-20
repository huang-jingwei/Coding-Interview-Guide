# 定义二叉树节点
class treeNode():
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# 函数功能：二叉树的中序遍历
def inorderPrint(root):
    if root == None:
        return []
    arr = []
    left = inorderPrint(root.left)
    if len(left) > 0:
        for node in left:
            arr.append(node)
    arr.append(root.val)
    right = inorderPrint(root.right)
    if len(right) > 0:
        for node in right:
            arr.append(node)
    return arr


# step1:获取输入数据
inf = list(map(int, input().split()))
n = inf[0]  # n 表示二叉树的总节点个数
root = inf[1]  # root 表示二叉树的根节点

# 获取二叉树节点信息
nodeArr = []
for i in range(n):
    node = list(map(int, input().split()))
    nodeArr.append(node)

# step2: 构建二叉树
# 初始化二叉树节点
node = {}
for index in range(n):
    node[nodeArr[index][0]] = treeNode(nodeArr[index][0])

# 初始化节点的左右儿子节点
for index in range(n):
    if nodeArr[index][1] != 0:
        node[nodeArr[index][0]].left = node[nodeArr[index][1]]
    if nodeArr[index][2] != 0:
        node[nodeArr[index][0]].right = node[nodeArr[index][2]]

# 二叉树头结点
head = node[root]

# step3：主函数入口
# 基本思路：搜索二叉子树的中序遍历数组是升序数组
count = 1
for index in range(n):
    curNode = node[nodeArr[index][0]]
    if curNode.left != None or curNode.left != None:
        inorder = inorderPrint(curNode)
        isBST = True

        num = len(inorder)
        if num > 1:
            for i in range(1, num):
                if inorder[i] <= inorder[i - 1]:
                    isBST = False
                    break

            if isBST == True and (num > count):
                count = num

print(count)