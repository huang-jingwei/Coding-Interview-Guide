# Coding-Interview-Guide
Python语言实现左程云《程序员代码面试指南》第二版

牛客网OJ：[程序员代码面试指南](https://www.nowcoder.com/ta/programmer-code-interview-guide?page=1)

因为牛客网OJ在链表、二叉树等相关题目均把题目数据以链表数据结构给出，略掉了二叉树、链表等结构的相关信息。这样不能准确评估是否已经正确解出题目。故下面除特殊说明，否则OJ链接均默认为LeetCode对应题目链接。 

## 第1章：栈和队列

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [设计一个有getMin功能的栈](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap1/01_MinStack.py) | [栈的最小值](https://leetcode-cn.com/problems/min-stack-lcci/) |
|    02    | [由两个栈组成的队列](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap1/02_MyQueue.py) | [用栈实现队列](https://leetcode-cn.com/problems/implement-queue-using-stacks/) |
|    03    |              如何仅用递归函数和栈操作逆序一个栈              |                                                              |
|    04    |                           猫狗队列                           |                                                              |
|    05    | [用一个栈实现另一个栈的排序](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap1/05_SortedStack.py) | [栈排序](https://leetcode-cn.com/problems/sort-of-stacks-lcci/) |
|    06    |                     用栈来求解汉诺塔问题                     |                                                              |
|    07    | [生成窗口最大值数组](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap1/07_maxSlidingWindow.py) | [滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum/) |
|    08    |                          单调栈结构                          | [单调栈结构(牛客网)](https://www.nowcoder.com/questionTerminal/e3d18ffab9c543da8704ede8da578b55) |
|    09    |                      求最大子矩阵的大小                      |                                                              |
|    10    |          最大值减去最小值小于或等于num的子数组数量           |                                                              |
|    11    |                        可见山峰对数量                        |                                                              |

## 第2章：链表问题

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [打印两个有序链表的公布部分](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/01_printCommonPart.py) | [打印两个有序链表的公布部分(牛客网)](https://www.nowcoder.com/practice/8943eea40dbb4185b187d80fd050fee9?tpId=101&&tqId=33116&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    02    | [在单链表和双链表中删除倒数第K个节点](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/02_removeNthFromEnd.py) | [ 删除链表的倒数第N个节点](https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list/) |
|    03    | [删除链表的中间节点和a/b处节点](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/03_deleteNode.py) | [删除中间节点](https://leetcode-cn.com/problems/delete-middle-node-lcci/) |
|    04    | [翻转单向和双向链表](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/04_reverseList.py) | [反转链表](https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof/) |
|    05    |                       翻转部分单向链表                       |                                                              |
|    06    |                    环形单链表的约瑟夫问题                    |                                                              |
|    07    | [判断一个链表是否为回文结构](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/07_isPalindrome.py) | [回文链表](https://leetcode-cn.com/problems/palindrome-linked-list/) |
|    08    | [将单向链表按某值划分为左边小、中间相等、右边大的形式](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/08_sortColors.py) |  [颜色分类](https://leetcode-cn.com/problems/sort-colors/)   |
|    09    | [复制含有随机指针节点的链表](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/09_copyRandomList.py) | [复杂链表的复制](https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/) |
|    10    | [两个单链表生成相加链表](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/10_addTwoNumbers.py) | [链表求和](https://leetcode-cn.com/problems/sum-lists-lcci/) |
|    11    | [两个单链表相交的一系列问题](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/11_getIntersectionNode.py) | [相交链表](https://leetcode-cn.com/problems/intersection-of-two-linked-lists/) |
|    12    |                 将单链表的每K个节点之间逆序                  | [K 个一组翻转链表](https://leetcode-cn.com/problems/reverse-nodes-in-k-group/) |
|    13    | [删除无序单链表中值重复出现的节点](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/13_deleteDuplicates.py) | [删除排序链表中的重复元素](https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list/) |
|    14    | [在单链表中删除指定值的节点](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/14_deleteNode.py) | [删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/) |
|    15    |                  将搜索二叉树转换成双向链表                  | [二叉搜索树与双向链表](https://leetcode-cn.com/problems/er-cha-sou-suo-shu-yu-shuang-xiang-lian-biao-lcof/) |
|    16    | [单链表的选择排序](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/16_insertionSortList.py) | [对链表进行插入排序](https://leetcode-cn.com/problems/insertion-sort-list/) |
|    17    | [一种怪异的节点删除方式](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/17_deleteNode.py) | [删除链表的节点](https://leetcode-cn.com/problems/shan-chu-lian-biao-de-jie-dian-lcof/) |
|    18    | [向有序的环形单链表中插入新节点](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/18_insertNode.py) | [向有序的环形单链表中插入新节点(牛客网)](https://www.nowcoder.com/practice/8a2ed8d048f241fd92b478140bad18a1?tpId=101&&tqId=33226&rp=1&ru=/ta/programmer-code-interview-guide&qru=/ta/programmer-code-interview-guide/question-ranking) |
|    19    | [合并两个有序的单链表](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap2/19_mergeTwoLists.py) | [合并两个有序链表](https://leetcode-cn.com/problems/merge-two-sorted-lists/) |
|    20    |               按照左右半区的方式重新组合单链表               |                                                              |

## 第3章：二叉树问题

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [分别用递归和非递归方式实现二叉树先序、中序和后序遍历](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/01_treePrint) | [二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/)、[二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/)、[二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/) |
|    02    |                       二叉树的最小深度                       | [二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree/)、[二叉树的最大深度](https://leetcode-cn.com/problems/maximum-depth-of-binary-tree/) |
|    03    |                   如何较为直观的打印二叉树                   |                                                              |
|    04    | [二叉树的序列化和反序列化](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap3/04_serialize_deserialize.py) | [二叉树的序列化与反序列化](https://leetcode-cn.com/problems/serialize-and-deserialize-binary-tree/) |
|    05    |                     遍历二叉树的神级方法                     |                                                              |
|    06    |          在二叉树中找到累加和为指定值的最长路径长度          |                                                              |
|    07    |                找到二叉树中的最大搜索二叉子树                |                                                              |
|    08    |         找到二叉树中符合搜索二叉树条件的最大拓扑结构         |                                                              |
|    09    | [二叉树的按层打印和ZigZag打印](https://github.com/gdutthu/Coding-Interview-Guide/tree/master/chap3/09_treePrint) | [二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal/) |
|    10    |                调整搜索二叉树中两个错误的节点                | [恢复二叉搜索树](https://leetcode-cn.com/problems/recover-binary-search-tree/) |
|    11    |              判断t1树是否包含t2树全部的拓扑结构              |                                                              |
|    12    |          判断t1树是否有与t2树拓扑结构完全相同的子树          |                                                              |
|    13    |                  判断二叉树是否为平衡二叉树                  |                                                              |
|    14    |                  根据后序数组重建搜索二叉树                  |                                                              |
|    15    |          判断一颗二叉树是否为搜索二叉树和完全二叉树          |                                                              |
|    16    |                通过有序数组生成平衡搜索二叉树                |                                                              |
|    17    |               在二叉树中找到一个节点的后继节点               |                                                              |
|    18    |             在二叉树中找到两个节点的最近公共祖先             |                                                              |
|    19    | Tarjan算法与并查集解决二叉树节点间最近公共祖先的批量查询问题 |                                                              |
|    20    |                  二叉树节点间的最大距离问题                  |                                                              |
|    21    |                       派对的最大快乐值                       |                                                              |
|    22    |              通过先序遍历和中序遍历生成后序数组              |                                                              |
|    23    |                  统计和生成所有不同的二叉树                  |                                                              |
|    24    |                    统计完全二叉树的节点数                    |                                                              |



## 第4章：递归和动态规划

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [斐波那契数列问题的递归和动态规划](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/01_fib.py) | [斐波那契数](https://leetcode-cn.com/problems/fibonacci-number/) |
|    02    | [矩阵的最小路径和](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/02_minPathSum.py) | [最小路径和](https://leetcode-cn.com/problems/minimum-path-sum/) |
|    03    | [换钱的最少货币数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/03_coinChange.py) |  [零钱兑换](https://leetcode-cn.com/problems/coin-change/)   |
|    04    |                   机器人到达指定位置方法数                   |                                                              |
|    05    | [换钱的方法数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap4/05_coinChange.py) | [零钱兑换 II](https://leetcode-cn.com/problems/coin-change-2/) |
|    06    |                       打气球的最大分数                       |                                                              |
|    07    |                        最长递增子序列                        |                                                              |
|    08    |                         信封嵌套问题                         |                                                              |
|    09    |                          汉诺塔问题                          |                                                              |
|    10    |                      最长公共子序列问题                      |                                                              |
|    11    |                       最长公共子串问题                       |                                                              |
|    12    |                   子数组异或为0的最多划分                    |                                                              |
|    13    |                        最小的编辑代价                        |                                                              |
|    14    |                       字符串的交错组成                       |                                                              |
|    15    |                      龙与地下城游戏问题                      | [地下城游戏](https://leetcode-cn.com/problems/dungeon-game/) |
|    16    |                数字字符串转换为字母组合的种数                |                                                              |
|    17    |                 表达式得到期望结果的组成种数                 |                                                              |
|    18    |                   排成一条线的纸牌博弈问题                   |                                                              |
|    19    |                           跳跃游戏                           | [跳跃游戏 II](https://leetcode-cn.com/problems/jump-game-ii/) |
|    20    |                      数组中最长连续序列                      |                                                              |
|    21    |                          N皇后问题                           |                                                              |

## 第8章：数组和矩阵问题

| 题目序号 |                        自己实现的题解                        |                            OJ链接                            |
| :------: | :----------------------------------------------------------: | :----------------------------------------------------------: |
|    01    | [转圈打印矩阵](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/01_spiralOrder.py) | [顺时针打印矩阵](https://leetcode-cn.com/problems/shun-shi-zhen-da-yin-ju-zhen-lcof/) |
|    02    | [将正方形矩阵顺时针转动90°](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/02_rotate.py) | [旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci/) |
|    03    | [”之“字型打印矩阵](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/03_findDiagonalOrder.py) | [对角线遍历](https://leetcode-cn.com/problems/diagonal-traverse/) |
|    04    | [找到无序数组中最小的k个数](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/04_getLeastNumbers.py) | [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/) |
|    05    | [需要排序的最短子数组长度](https://github.com/gdutthu/Coding-Interview-Guide/blob/master/chap8/05_findUnsortedSubarray.py) | [最短无序连续子数组](https://leetcode-cn.com/problems/shortest-unsorted-continuous-subarray/) |
|    06    |               在数组中找到出现次数大于N/K的数                |                                                              |
|    07    |                在行列都排好序的矩阵中找指定数                |                                                              |
|    08    |                   最长的可整合子数组的长度                   |                                                              |
|    09    |    不重复打印排序数组中相加和为给定值得所有二元组和三元组    |                                                              |
|    10    |         未排序正数组中累加和为给定值的最长子数组长度         |                                                              |
|    11    |        未排序数组中累加和为给定值的最长子数组系列问题        |                                                              |
|    12    |       未排序数组中累加小于或等于给定值的最长子数组长度       |                                                              |
|    13    |                        计算数组的小和                        |                                                              |
|    14    |                       自然数数组的排序                       |                                                              |
|    15    |              奇数下标都是奇数或偶数下标都是偶数              |                                                              |
|    16    |                    子数组的最大累加和问题                    |                                                              |
|    17    |                    子矩阵的最大累加和问题                    |                                                              |
|    18    |                在数组中找到一个局部最小的位置                |                                                              |
|    19    |                   数组中子数组的最大累乘积                   |                                                              |
|    20    |                  打印N个数组整体最大的Top K                  |                                                              |
|    21    |                  边界都是1的最大正方形大小                   |                                                              |
|    22    |                    不包含本位置的累乘数组                    |                                                              |
|    23    |                     数组的partition调整                      |                                                              |
|    24    |                         求最短通路值                         |                                                              |
|    25    |                   数组中未出现的最小正整数                   |                                                              |
|    26    |                 数组排序之后相邻数的最大差值                 |                                                              |
|    27    |                     做项目的最大收益问题                     |                                                              |
|    28    |                       分金条的最小花费                       |                                                              |
|    29    |                         大楼轮廓问题                         |                                                              |
|    30    |                     加油站良好出发点问题                     |                                                              |
|    31    |                         容器盛水问题                         |                                                              |

