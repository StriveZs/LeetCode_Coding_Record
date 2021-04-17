---
title: LeetCode No.86

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第八十六题题—分隔链表
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

 ![figure.1](https://assets.leetcode.com/uploads/2021/01/04/partition.jpg)
 
```
示例 1：

输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]
 
提示：

链表中节点的数目在范围 [0, 200] 内
-100 <= Node.val <= 100
-200 <= x <= 200
```

## 代码
```
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode

        核心思想：大于x的第一个节点后面小于x的节点全部放到第一个节点前面(保持节点间的相对位置不变，不需要排序)
                1.小于 x 部分的链表按照原始顺序 记为 p
                2.大于等于 x 部分的链表按照原始顺序 记为 q
                3.拼接两个链表，p --> q
        """
        a = left = ListNode()
        b = right = ListNode()
        while head != None:
            if head.val < x:
                left.next = head
                left = left.next
            else:
                right.next = head
                right = right.next
            head = head.next
        left.next = b.next # 拼接
        right.next = None
        return a.next
```