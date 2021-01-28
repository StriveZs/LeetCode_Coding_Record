---
title: LeetCode No.24

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第二十四题

## 题目描述
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/0vYhrJ.jpg)

```
示例 1：

输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
 
提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
```

## 代码
除了本题的办法，同样也可以采用递归的方法进行操作，因此都是相同的操作。

```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None

        if head.next == None:
            return head

        res = ListNode(None)
        res = head

        while True:
            if head == None:
                break
            if head.next == None:
                break
            temp = head.val
            nextNode = head.next
            head.val = nextNode.val
            nextNode.val = temp
            head = head.next.next
        return res
```