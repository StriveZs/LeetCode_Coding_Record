---
title: LeetCode No.142

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第142题—环形链表II
即将回家！

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个链表，返回链表开始入环的第一个节点。 如果链表无环，则返回 null。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。注意，pos 仅仅是用于标识环的情况，并不会作为参数传递到函数中。

说明：不允许修改给定的链表。

进阶：

你是否可以使用 O(1) 空间解决此题？

![figure.1](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist.png)
 
```
示例 1：

输入：head = [3,2,0,-4], pos = 1
输出：返回索引为 1 的链表节点
解释：链表中有一个环，其尾部连接到第二个节点。
```
![figure.2](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test2.png)
```
示例 2：

输入：head = [1,2], pos = 0
输出：返回索引为 0 的链表节点
解释：链表中有一个环，其尾部连接到第一个节点。
```
![figure.3](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/07/circularlinkedlist_test3.png)
```
示例 3：

输入：head = [1], pos = -1
输出：返回 null
解释：链表中没有环。
 
提示：

链表中节点的数目范围在范围 [0, 104] 内
-105 <= Node.val <= 105
pos 的值为 -1 或者链表中的一个有效索引
```
## 代码
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    return_node = None
    flag = True
    def detectCycle(self, head):
        """
        dfs遍历，返回环的第一个节点就好了
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return None
        self.return_node = None
        self.flag = True # 结束标志
        meomory = [] # 记忆列表

        def dfs(node):
            if self.flag:
                if node is not None:
                    if node in meomory:
                        self.return_node = node
                        self.flag = False
                    meomory.append(node)
                    dfs(node.next)

        dfs(head)
        return self.return_node
```