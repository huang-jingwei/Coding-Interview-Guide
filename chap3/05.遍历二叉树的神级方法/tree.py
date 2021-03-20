# 二叉树节点
class treeNode():
    def __init__(self,val):
        self.val=val
        self.left=None
        self.right=None

# 函数功能：二叉树的前序遍历
def treePrePrint(root):
    if root==None:
        return []
    arr=[]
    arr.append(root.val)

    left=treePrePrint(root.left)
    if len(left)>0:
        for node in left:
            arr.append(node)
    right=treePrePrint(root.right)
    if len(right)>0:
        for node in right:
            arr.append(node)
    return arr


# 函数功能：二叉树的中序遍历
def treeInorderPrint(root):
    if root==None:
        return []
    arr=[]

    left = treeInorderPrint(root.left)
    if len(left) > 0:
        for node in left:
            arr.append(node)
    arr.append(root.val)
    right = treeInorderPrint(root.right)
    if len(right) > 0:
        for node in right:
            arr.append(node)
    return arr


# 函数功能：二叉树的后序遍历
def treePostPrint(root):
    if root == None:
        return []
    arr = []
    left = treePostPrint(root.left)
    if len(left) > 0:
        for node in left:
            arr.append(node)
    right = treePostPrint(root.right)
    if len(right) > 0:
        for node in right:
            arr.append(node)
    arr.append(root.val)
    return arr


# step1：获取输入数据
inf = list(map(int, input().split()))
n = inf[0]     # n 表示二叉树的总节点个数
root = inf[1]  # root 表示二叉树的根节点

arr = []
for i in range(n):
    node = list(map(int, input().split()))
    arr.append(node)

# step2:定义二叉树
node={}
# 初始化二叉树节点
for index in range(n):
    node[arr[index][0]]=treeNode(arr[index][0])
# 初始化二叉树的左右儿子节点
for index in range(n):
    if arr[index][1] !=0:
        node[arr[index][0]].left=node[arr[index][1]]

    if arr[index][2] !=0:
        node[arr[index][0]].right=node[arr[index][2]]


# step2:分别进行二叉树的前序、中序、后序遍历
# 特别注意，节点下标是从1开始计算
head=node[root]
pre = treePrePrint(head)
inorder = treeInorderPrint(head)
post = treePostPrint(head)

# step3:打印结果
for index in range(len(pre)):
    print(pre[index], end=" ")
print("")  # 输出换行
for index in range(len(inorder)):
    print(inorder[index], end=" ")
print("")  # 输出换行
for index in range(len(post)):
    print(post[index], end=" ")