---
title: LeetCode No.19

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第十九题
## 题目描述
给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。

进阶：你能尝试使用一趟扫描实现吗？

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/OMbmD5.jpg)

```
示例 1：

输入：head = [1,2,3,4,5], n = 2
输出：[1,2,3,5]
示例 2：

输入：head = [1], n = 1
输出：[]
示例 3：

输入：head = [1,2], n = 1
输出：[1]
 

提示：

链表中结点的数目为 sz
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz
```

## 代码
```
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        """
            基本思想：由于是寻找从后往前数第n个，因此第一遍先正数n个，然后第二遍再从头开始往后遍历同时第一遍正数的从n开始为空之后，这样第二遍数的就变为到空还有n个
            然后在去掉第倒数n个节点就行了。
        """
        a = head
        b = head
        # 第一遍数n个
        for i in range(n):
            if a.next:
                a = a.next
            else:
                return head.next
        # 接着数第一遍的同时，第二遍从头开始
        while a.next:
            a = a.next
            b = b.next
        b.next = b.next.next
        return head

```