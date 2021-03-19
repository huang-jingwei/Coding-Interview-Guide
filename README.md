# Coding-Interview-Guide
左程云《程序员代码面试指南》第二版编程题的Python语言实现

牛客网OJ：[程序员代码面试指南](https://www.nowcoder.com/ta/programmer-code-interview-guide?page=1)

LeetCode：https://leetcode-cn.com/problemset/all/



因为牛客网OJ在链表、二叉树等相关题目均把题目数据以链表数据结构给出，略掉了二叉树、链表等结构的相关信息。这样不能准确评估是否已经正确解出题目。故下面除特殊说明，否则OJ链接均默认为LeetCode对应题目链接。 

## [第1章：栈和队列](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1)

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [设计一个有getMin功能的栈](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/01.%E8%AE%BE%E8%AE%A1%E4%B8%80%E4%B8%AA%E6%9C%89getMin%E5%8A%9F%E8%83%BD%E7%9A%84%E6%A0%88) | [栈的最小值](https://leetcode-cn.com/problems/min-stack-lcci/) |
|    02    | [由两个栈组成的队列](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/02.%E7%94%B1%E4%B8%A4%E4%B8%AA%E6%A0%88%E7%BB%84%E6%88%90%E7%9A%84%E9%98%9F%E5%88%97) | [用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/) |
|    03    | [如何仅用递归函数和栈操作逆序一个栈](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/03.%E5%A6%82%E4%BD%95%E4%BB%85%E7%94%A8%E9%80%92%E5%BD%92%E5%87%BD%E6%95%B0%E5%92%8C%E6%A0%88%E6%93%8D%E4%BD%9C%E9%80%86%E5%BA%8F%E4%B8%80%E4%B8%AA%E6%A0%88) | [用递归函数和栈操作逆序一个栈(牛客)](https://www.nowcoder.com/practice/1de82c89cc0e43e9aa6ee8243f4dbefd?tpId=101&tqId=33075&rp=1&ru=%2Fta%2Fprogrammer-code-interview-guide&qru=%2Fta%2Fprogrammer-code-interview-guide%2Fquestion-ranking&tab=answerKey) |
|    04    |                           猫狗队列                           |                                                              |
|    05    | [用一个栈实现另一个栈的排序](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/05.%E7%94%A8%E4%B8%80%E4%B8%AA%E6%A0%88%E5%AE%9E%E7%8E%B0%E5%8F%A6%E4%B8%80%E4%B8%AA%E6%A0%88%E7%9A%84%E6%8E%92%E5%BA%8F) | [栈排序](https://leetcode-cn.com/problems/sort-of-stacks-lcci/) |
|    06    | [用栈来求解汉诺塔问题](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/06.%E7%94%A8%E6%A0%88%E6%9D%A5%E6%B1%82%E8%A7%A3%E6%B1%89%E8%AF%BA%E5%A1%94%E9%97%AE%E9%A2%98) | [面试题 08.06. 汉诺塔问题](https://leetcode-cn.com/problems/hanota-lcci/) |
|    07    | [生成窗口最大值数组](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/07.%E7%94%9F%E6%88%90%E7%AA%97%E5%8F%A3%E6%9C%80%E5%A4%A7%E5%80%BC%E6%95%B0%E7%BB%84) | [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) |
|    08    | [单调栈结构](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/08.%E5%8D%95%E8%B0%83%E6%A0%88%E7%BB%93%E6%9E%84) | [单调栈结构(牛客网)](https://www.nowcoder.com/questionTerminal/e3d18ffab9c543da8704ede8da578b55) |
|    09    | [求最大子矩阵的大小](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/09.%E6%B1%82%E6%9C%80%E5%A4%A7%E5%AD%90%E7%9F%A9%E9%98%B5%E7%9A%84%E5%A4%A7%E5%B0%8F) | [最大矩形](https://leetcode-cn.com/problems/maximal-rectangle/) |
|    10    | [最大值减去最小值小于或等于num的子数组数量](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap1/10.%E6%9C%80%E5%A4%A7%E5%80%BC%E5%87%8F%E5%8E%BB%E6%9C%80%E5%B0%8F%E5%80%BC%E5%B0%8F%E4%BA%8E%E6%88%96%E7%AD%89%E4%BA%8Enum%E7%9A%84%E5%AD%90%E6%95%B0%E7%BB%84%E6%95%B0%E9%87%8F) | [最大值减去最小值小于或等于num的子数组数量(牛客)](https://www.nowcoder.com/practice/5fe02eb175974e18b9a546812a17428e?tpId=101&tqId=33086&rp=1&ru=%2Fta%2Fprogrammer-code-interview-guide&qru=%2Fta%2Fprogrammer-code-interview-guide%2Fquestion-ranking&tab=answerKey) |
|    11    |                        可见山峰对数量                        |                                                              |

## [第2章：链表问题](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2)

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [打印两个有序链表的公布部分](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/01.%E6%89%93%E5%8D%B0%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E9%93%BE%E8%A1%A8%E7%9A%84%E5%85%AC%E5%B8%83%E9%83%A8%E5%88%86) | [打印两个有序链表的公布部分(牛客网)](https://www.nowcoder.com/practice/8943eea40dbb4185b187d80fd050fee9?tpId=101&&tqId=33116&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    02    | [在单链表和双链表中删除倒数第K个节点](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/02.%E5%9C%A8%E5%8D%95%E9%93%BE%E8%A1%A8%E5%92%8C%E5%8F%8C%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%88%A0%E9%99%A4%E5%80%92%E6%95%B0%E7%AC%ACK%E4%B8%AA%E8%8A%82%E7%82%B9) | [ 删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) |
|    03    | [删除链表的中间节点和a/b处节点](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/03.%E5%88%A0%E9%99%A4%E9%93%BE%E8%A1%A8%E7%9A%84%E4%B8%AD%E9%97%B4%E8%8A%82%E7%82%B9%E5%92%8Cab%E5%A4%84%E8%8A%82%E7%82%B9) | [删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci/) |
|    04    | [翻转单向和双向链表](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/04.%E7%BF%BB%E8%BD%AC%E5%8D%95%E5%90%91%E5%92%8C%E5%8F%8C%E5%90%91%E9%93%BE%E8%A1%A8) | [反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/) |
|    05    |                       翻转部分单向链表                       |                                                              |
|    06    |                    环形单链表的约瑟夫问题                    |                                                              |
|    07    | [判断一个链表是否为回文结构](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/07.%E5%88%A4%E6%96%AD%E4%B8%80%E4%B8%AA%E9%93%BE%E8%A1%A8%E6%98%AF%E5%90%A6%E4%B8%BA%E5%9B%9E%E6%96%87%E7%BB%93%E6%9E%84) | [回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/) |
|    08    | [将单向链表按某值划分为左边小、中间相等、右边大的形式](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/08.%E5%B0%86%E5%8D%95%E5%90%91%E9%93%BE%E8%A1%A8%E6%8C%89%E6%9F%90%E5%80%BC%E5%88%92%E5%88%86%E4%B8%BA%E5%B7%A6%E8%BE%B9%E5%B0%8F%E3%80%81%E4%B8%AD%E9%97%B4%E7%9B%B8%E7%AD%89%E3%80%81%E5%8F%B3%E8%BE%B9%E5%A4%A7%E7%9A%84%E5%BD%A2%E5%BC%8F) |  [颜色分类](https://leetcode-cn.com/problems/sort-colors/)   |
|    09    | [复制含有随机指针节点的链表](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/09.%E5%A4%8D%E5%88%B6%E5%90%AB%E6%9C%89%E9%9A%8F%E6%9C%BA%E6%8C%87%E9%92%88%E8%8A%82%E7%82%B9%E7%9A%84%E9%93%BE%E8%A1%A8) | [复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/) |
|    10    | [两个单链表生成相加链表](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/10.%E4%B8%A4%E4%B8%AA%E5%8D%95%E9%93%BE%E8%A1%A8%E7%94%9F%E6%88%90%E7%9B%B8%E5%8A%A0%E9%93%BE%E8%A1%A8) | [链表求和](https://leetcode-cn.com/problems/sum-lists-lcci/) |
|    11    | [两个单链表相交的一系列问题](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/11.%E4%B8%A4%E4%B8%AA%E5%8D%95%E9%93%BE%E8%A1%A8%E7%9B%B8%E4%BA%A4%E7%9A%84%E4%B8%80%E7%B3%BB%E5%88%97%E9%97%AE%E9%A2%98) | [相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/) |
|    12    |                 将单链表的每K个节点之间逆序                  | [K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/) |
|    13    | [删除无序单链表中值重复出现的节点](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/13.%E5%88%A0%E9%99%A4%E6%97%A0%E5%BA%8F%E5%8D%95%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%80%BC%E9%87%8D%E5%A4%8D%E5%87%BA%E7%8E%B0%E7%9A%84%E8%8A%82%E7%82%B9) | [删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/) |
|    14    | [在单链表中删除指定值的节点](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/14.%E5%9C%A8%E5%8D%95%E9%93%BE%E8%A1%A8%E4%B8%AD%E5%88%A0%E9%99%A4%E6%8C%87%E5%AE%9A%E5%80%BC%E7%9A%84%E8%8A%82%E7%82%B9) | [删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/) |
|    15    |                  将搜索二叉树转换成双向链表                  | [二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/) |
|    16    | [单链表的选择排序](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/16.%E5%8D%95%E9%93%BE%E8%A1%A8%E7%9A%84%E9%80%89%E6%8B%A9%E6%8E%92%E5%BA%8F) | [对链表进行插入排序](https://leetcode-cn.com/problems/insertion-sort-list/) |
|    17    | [一种怪异的节点删除方式](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/17.%E4%B8%80%E7%A7%8D%E6%80%AA%E5%BC%82%E7%9A%84%E8%8A%82%E7%82%B9%E5%88%A0%E9%99%A4%E6%96%B9%E5%BC%8F) | [删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/) |
|    18    | [向有序的环形单链表中插入新节点](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/18.%E5%90%91%E6%9C%89%E5%BA%8F%E7%9A%84%E7%8E%AF%E5%BD%A2%E5%8D%95%E9%93%BE%E8%A1%A8%E4%B8%AD%E6%8F%92%E5%85%A5%E6%96%B0%E8%8A%82%E7%82%B9) | [向有序的环形单链表中插入新节点(牛客网)](https://www.nowcoder.com/practice/8a2ed8d048f241fd92b478140bad18a1?tpId=101&&tqId=33226&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    19    | [合并两个有序的单链表](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap2/19.%E5%90%88%E5%B9%B6%E4%B8%A4%E4%B8%AA%E6%9C%89%E5%BA%8F%E7%9A%84%E5%8D%95%E9%93%BE%E8%A1%A8) | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) |
|    20    |               按照左右半区的方式重新组合单链表               |                                                              |

## [第3章：二叉树问题](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3)

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [分别用递归和非递归方式实现二叉树先序、中序和后序遍历](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/01_treePrint) | [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)、[二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)、[二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/) |
|    02    | [二叉树的最小深度](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/02_minDepth) | [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)、[二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) |
|    03    |                   如何较为直观的打印二叉树                   |                                                              |
|    04    | [二叉树的序列化和反序列化](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/04_serialize_deserialize.py) | [二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/) |
|    05    |              遍历二叉树的神级方法（Morris遍历）              |                                                              |
|    06    | [在二叉树中找到累加和为指定值的最长路径长度](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/06_pathSum.py) | [二叉树中和为某一值的路径](https://leetcode-cn.com/problems/er-cha-shu-zhong-he-wei-mou-yi-zhi-de-lu-jing-lcof/) |
|    07    |                找到二叉树中的最大搜索二叉子树                |               只有leetcode会员才能测试o(╯□╰)o                |
|    08    |         找到二叉树中符合搜索二叉树条件的最大拓扑结构         |                                                              |
|    09    | [二叉树的按层打印和ZigZag打印](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/09_treePrint) | [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) |
|    10    |                调整搜索二叉树中两个错误的节点                | [恢复二叉搜索树](https://leetcode-cn.com/problems/recover-binary-search-tree/) |
|    11    | [判断t1树是否包含t2树全部的拓扑结构](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/11_isSubStructure.py) | [树的子结构](https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/) |
|    12    | [判断t1树是否有与t2树拓扑结构完全相同的子树](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/12_isSubtree.py) | [另一个树的子树](https://leetcode-cn.com/problems/subtree-of-another-tree/) |
|    13    | [判断二叉树是否为平衡二叉树](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/13_isBalanced.py) | [平衡二叉树](https://leetcode-cn.com/problems/balanced-binary-tree/) |
|    14    | [根据后序数组重建搜索二叉树](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/14_verifyPostorder) | [二叉搜索树的后序遍历序列](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/) |
|    15    | [判断一颗二叉树是否为搜索二叉树和完全二叉树](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/15_isValidBST) | [验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree/)、[二叉树的完全性检验](https://leetcode-cn.com/problems/check-completeness-of-a-binary-tree/) |
|    16    | [通过有序数组生成平衡搜索二叉树](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/16_sortedArrayToBST.py) | [将有序数组转换为二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree/) |
|    17    | [在二叉树中找到一个节点的后继节点](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/17_inorderSuccessor.py) |  [后继者](https://leetcode-cn.com/problems/successor-lcci/)  |
|    18    | [在二叉树中找到两个节点的最近公共祖先](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/18_lowestCommonAncestor) | [二叉搜索树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-search-tree/)、[二叉树的最近公共祖先](https://leetcode-cn.com/problems/er-cha-shu-de-zui-jin-gong-gong-zu-xian-lcof/) |
|    19    | Tarjan算法与并查集解决二叉树节点间最近公共祖先的批量查询问题 |                                                              |
|    20    | [二叉树节点间的最大距离问题](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/20_diameterOfBinaryTree.py) | [二叉树的直径](https://leetcode-cn.com/problems/diameter-of-binary-tree/) |
|    21    |                       派对的最大快乐值                       |                                                              |
|    22    | [通过先序遍历和中序遍历生成后序数组](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/22_buildTree) | [从中序与后序遍历序列构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)、[根据前序和后序遍历构造二叉树](https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/) |
|    23    |                  统计和生成所有不同的二叉树                  | [不同的二叉搜索树](https://leetcode-cn.com/problems/unique-binary-search-trees/)、[不同的二叉搜索树 II](https://leetcode-cn.com/problems/unique-binary-search-trees-ii/) |
|    24    | [统计完全二叉树的节点数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/24_countNodes.py) | [完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes/) |



## [第4章：递归和动态规划](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap4)

备注：

1、第4题牛客网的OJ测试有问题，按照书本解法，只能过40％的case

2、第5题没做优化，

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [斐波那契数列问题的递归和动态规划](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/01_fib.py) | [斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/) |
|    02    | [矩阵的最小路径和](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/02_minPathSum.py) | [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/) |
|    03    | [换钱的最少货币数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/03_coinChange.py) |  [零钱兑换](https://leetcode-cn.com/problems/coin-change/)   |
|    04    | [机器人到达指定位置方法数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/04_wayCounts.py) | [机器人到达指定位置方法数（牛客）](https://www.nowcoder.com/practice/54679e44604f44d48d1bcadb1fe6eb61?tpId=101&&tqId=33085&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    05    | [换钱的方法数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/05_coinChange.py) | [零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/) |
|    06    |                       打气球的最大分数                       |                                                              |
|    07    | [最长递增子序列](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/07_findNumberOfLIS.py) | [最长递增子序列的个数](https://leetcode-cn.com/problems/number-of-longest-increasing-subsequence/) |
|    08    |                         信封嵌套问题                         |                                                              |
|    09    |                          汉诺塔问题                          |                                                              |
|    10    | [最长公共子序列问题](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/10_longestCommonSubsequence.py) | [最长公共子序列](https://leetcode-cn.com/problems/longest-common-subsequence/) |
|    11    |                       最长公共子串问题                       |                                                              |
|    12    |                   子数组异或为0的最多划分                    |                                                              |
|    13    |                        最小的编辑代价                        |                                                              |
|    14    |                       字符串的交错组成                       |                                                              |
|    15    |                      龙与地下城游戏问题                      | [地下城游戏](https://leetcode-cn.com/problems/dungeon-game/) |
|    16    |                数字字符串转换为字母组合的种数                |                                                              |
|    17    |                 表达式得到期望结果的组成种数                 |                                                              |
|    18    |                   排成一条线的纸牌博弈问题                   |                                                              |
|    19    |                           跳跃游戏                           | [跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/) |
|    20    |                      数组中最长连续序列                      | [最长连续序列](https://leetcode-cn.com/problems/longest-consecutive-sequence/) |
|    21    |                          N皇后问题                           |                                                              |

##  [第5章：字符串问题](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap5)

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [判断两个字符串是否互为变形词](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/01_isDeformation.py) | [判断两个字符串是否互为变形词(牛客)](https://www.nowcoder.com/practice/b07c464a107e421ebbd2c82aebd42e39?tpId=101&&tqId=33163&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    02    | [判断两个字符串是否互为旋转词](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/02_chkRotation.py) | [判断两个字符串是否互为旋转词(牛客)](https://www.nowcoder.com/practice/687deda2cc57473499e058207f6258cf?tpId=101&&tqId=33164&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    03    |                    将整数字符串转成整数值                    |                                                              |
|    04    |                      字符串的统计字符串                      |                                                              |
|    05    | [判断字符串数组中是否所有的字符都只出现过一次](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/05_stringIsUnique.py) |             牛客网和LeetCode OJ均找不到这个题目              |
|    06    | [在有序但含有空的数组中查找字符串](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/06_getIndex.py) | [在有序但含有空的数组中查找字符串(牛客网)](https://www.nowcoder.com/practice/92c172ef7c6d4ccc8f3103c3bc36cae2?tpId=101&&tqId=33167&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    07    | [字符串的调整与替换](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/07_replaceSpace.py) | [替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/) |
|    08    | [翻转字符串](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/08_reverseWords.py) | [翻转单词顺序](https://leetcode-cn.com/problems/fan-zhuan-dan-ci-shun-xu-lcof/) |
|    09    |                         完美洗牌问题                         |                                                              |
|    10    |              删除多余字符得到字典序最小的字符串              |                                                              |
|    11    |                  数组中两个字符串的最小距离                  |                                                              |
|    12    |                     字符串的转换路径问题                     |                                                              |
|    13    | [添加最少字符使字符串整体都是回文字符串](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/13_minInsertions.py) | [让字符串成为回文串的最少插入次数](https://leetcode-cn.com/problems/minimum-insertion-steps-to-make-a-string-palindrome/) |
|    14    |               括号字符串的有效性和最长有效长度               |                                                              |
|    15    |                        公式字符串求值                        |                                                              |
|    16    |                 0左边必有1的二进制字符串数量                 |                                                              |
|    17    |          拼接所有字符串产生字典顺序最小的大写字符串          |                                                              |
|    18    | [找到字符串的最长无重复字符子串](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/18_lengthOfLongestSubstring.py) | [最长不含重复字符的子字符串](https://leetcode-cn.com/problems/zui-chang-bu-han-zhong-fu-zi-fu-de-zi-zi-fu-chuan-lcof/) |
|    19    |                     找到指定的新类型字符                     |                                                              |
|    20    |                        旋变字符串问题                        |                                                              |
|    21    |                      最小包含子串的长度                      | [最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/) |
|    22    |                        回文最少分割数                        |                                                              |
|    23    |                        字符串匹配问题                        |                                                              |
|    24    | [字典树（前缀树）的实现](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap5/24_Trie.py) | [实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/) |
|    25    |                      子数组的最大异或和                      | [子数组最大异或和(牛客网)](https://www.nowcoder.com/practice/43f62c52fbac47feaeabe40ac1ab9091?tpId=101&tqId=33209&tPage=1&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking)，[数组中两个数的最大异或值](https://leetcode-cn.com/problems/maximum-xor-of-two-numbers-in-an-array/) |

## [第8章：数组和矩阵问题](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap8)

第5题还没做完，第6题的进阶问题还没做完。

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [转圈打印矩阵](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/01_spiralOrder.py) | [顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/) |
|    02    | [将正方形矩阵顺时针转动90°](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/02_rotate.py) | [旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci/) |
|    03    | [”之“字型打印矩阵](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/03_findDiagonalOrder.py) | [对角线遍历](https://leetcode-cn.com/problems/diagonal-traverse/) |
|    04    | [找到无序数组中最小的k个数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/04_getLeastNumbers.py) | [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/) |
|    05    | [需要排序的最短子数组长度](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/05_findUnsortedSubarray.py) | [最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/) |
|    06    | [在数组中找到出现次数大于N/K的数](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap8/06_majorityElement) | [数组中出现次数超过一半的数字](https://leetcode-cn.com/problems/shu-zu-zhong-chu-xian-ci-shu-chao-guo-yi-ban-de-shu-zi-lcof/)、[求众数 II](https://leetcode-cn.com/problems/majority-element-ii/) |
|    07    | [在行列都排好序的矩阵中找指定数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/07_findNumberIn2DArray.py) | [二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof/) |
|    08    |                   最长的可整合子数组的长度                   |                                                              |
|    09    | [不重复打印排序数组中相加和为给定值得所有二元组和三元组](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap8/09_numSum) | [和为s的两个数字](https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/) |
|    10    |         未排序正数组中累加和为给定值的最长子数组长度         | [未排序正数组中累加和为给定值的最长子数组长度(牛客网)](https://www.nowcoder.com/practice/a4e34287fa1b41f9bd41f957efbd5dff?tpId=101&&tqId=33076&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    11    |        未排序数组中累加和为给定值的最长子数组系列问题        |                                                              |
|    12    |       未排序数组中累加小于或等于给定值的最长子数组长度       |                                                              |
|    13    |                        计算数组的小和                        |                                                              |
|    14    |                       自然数数组的排序                       |                                                              |
|    15    |              奇数下标都是奇数或偶数下标都是偶数              | [奇数下标都是奇数或偶数下标都是偶数(牛客网)](https://www.nowcoder.com/practice/335823db14b945ab95241a74cfcf1ae7?tpId=101&&tqId=33092&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    16    | [子数组的最大累加和问题](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/16_maxSubArray.py) | [连续子数组的最大和](https://leetcode-cn.com/problems/lian-xu-zi-shu-zu-de-zui-da-he-lcof/) |
|    17    |                    子矩阵的最大累加和问题                    |                                                              |
|    18    |                在数组中找到一个局部最小的位置                |                                                              |
|    19    |                   数组中子数组的最大累乘积                   | [乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray/) |
|    20    | [打印N个数组整体最大的Top K](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/20_getLeastNumbers.py) | [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/) |
|    21    |                  边界都是1的最大正方形大小                   |                                                              |
|    22    | [不包含本位置的累乘数组](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/22_constructArr.py) | [构建乘积数组](https://leetcode-cn.com/problems/gou-jian-cheng-ji-shu-zu-lcof/) |
|    23    |                     数组的partition调整                      |                                                              |
|    24    |                         求最短通路值                         |                                                              |
|    25    | [数组中未出现的最小正整数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/25_firstMissingPositive.py) | [缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive/) |
|    26    | [数组排序之后相邻数的最大差值](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/26_maximumGap.py) |  [最大间距](https://leetcode-cn.com/problems/maximum-gap/)   |
|    27    | [做项目的最大收益问题](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/27_findMaximizedCapital.py) | [IPO](https://leetcode-cn.com/problems/ipo/)（备注：思路没问题，但是会超出时间限制，还得进一步优化） |
|    28    |                       分金条的最小花费                       |                                                              |
|    29    |                         大楼轮廓问题                         |                                                              |
|    30    |                     加油站良好出发点问题                     |                                                              |
|    31    |                         容器盛水问题                         |                                                              |

## [第9章：其他题目](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap9)

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    |                    从5随机到7随机及其扩展                    |                                                              |
|    02    |                   一行代码求两个数的公约数                   |                                                              |
|    03    |                      有关阶乘的两个问题                      |                                                              |
|    04    |                   判断一个点是否在矩形内部                   |                                                              |
|    05    |                  判断一个点是否在三角形内部                  |                                                              |
|    06    |                           折纸问题                           |                                                              |
|    07    |                      能否完美地拼成矩形                      |                                                              |
|    08    |                          蓄水池问题                          |                                                              |
|    09    |                   设计有setAll功能的哈希表                   |                                                              |
|    11    |             最大的leftMax与rightMax之差的绝对值              | [最大的leftMax与rightMax之差的绝对值(牛客网)](https://www.nowcoder.com/practice/0639c9c82ca643d0b08a58ae40cad178?tpId=101&&tqId=33131&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    12    | [设计LRU缓存结构](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap9/12_LRUCache.py) |  [LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/)  |
|    13    |                       LFU缓存结构设计                        |                                                              |
|    14    | [设计RamdomPool结构](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap9/14_RandomizedCollection) | [常数时间插入、删除和获取随机元素](https://leetcode-cn.com/problems/insert-delete-getrandom-o1/)、[O(1) 时间插入、删除和获取随机元素 - 允许重复](https://leetcode-cn.com/problems/insert-delete-getrandom-o1-duplicates-allowed/) |
|    15    | [并查集的实现](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap9/15_numIslands.py) | [岛屿数量](https://leetcode-cn.com/problems/number-of-islands/) |
|    16    |                调整[0,x)区间上的数出现的概率                 |                                                              |
|    17    |                     路径数组变为统计数组                     |                                                              |
|    18    |                   正数数组的最小不可组成和                   |                                                              |
|    19    |             累加出整个范围所有的数最少还需几个数             |                                                              |
|    20    |                  一种字符串和数字的对应关系                  |                                                              |
|    21    |                      1到n中1出现的次数                       | [1～n 整数中 1 出现的次数](https://leetcode-cn.com/problems/1nzheng-shu-zhong-1chu-xian-de-ci-shu-lcof/) |
|    22    |                   从N个数中等概率打印M个数                   |                                                              |
|    23    | [判断一个数是否是回文数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap9/23_isPalindrome.py) | [回文数](https://leetcode-cn.com/problems/palindrome-number/) |
|    24    | [在有序旋转数组中找到最小值](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap9/24_findMin.py) | [寻找旋转排序数组中的最小值 II](https://leetcode-cn.com/problems/find-minimum-in-rotated-sorted-array-ii/) |
|    25    | [在有序旋转数组中找到一个数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap9/25_search.py) | [搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/) |
|    26    |                   数字的英文表达和正文表达                   |                                                              |
|    27    |                          分糖果问题                          |                                                              |
|    28    |                 一种消息接收并打印的结构设计                 |                                                              |
|    29    | [随时找到数据流的中位数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap9/29_MedianFinder.py) | [数据流的中位数](https://leetcode-cn.com/problems/find-median-from-data-stream/) |
|    30    | [在两个长度相等的排序数组中找到中位数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap9/30_findMedianSortedArrays.py) | [寻找两个正序数组的中位数](https://leetcode-cn.com/problems/median-of-two-sorted-arrays/) |
|    31    |                在两个排序数组中找到第k小的数                 |           在LeetCode里面，30和31题都是同样一道题目           |
|    32    |               两个有序数组间相加和的Top k问题                |                                                              |
|    33    | [出现次数的Top k问题](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap9/33_topKFrequent.py) | [前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/) |
|    34    |                         Manacher算法                         |                                                              |
|    35    |                           KMP算法                            |                                                              |
|    36    |                          丢棋子问题                          |                                                              |
|    37    |                           画匠问题                           |                                                              |
|    38    |                         邮局选址问题                         |                                                              |

