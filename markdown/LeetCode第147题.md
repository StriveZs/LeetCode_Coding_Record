---
title: LeetCode No.147

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第147题—对链表进行插入排序

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
对链表进行插入排序。


插入排序的动画演示如上。从第一个元素开始，该链表可以被认为已经部分排序（用黑色表示）。
每次迭代时，从输入数据中移除一个元素（用红色表示），并原地将其插入到已排好序的链表中。

 

插入排序算法：

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。

``` 
示例 1：

输入: 4->2->1->3
输出: 1->2->3->4
示例 2：

输入: -1->5->3->4->0
输出: -1->0->3->4->5
```
## 插入排序原理
用一张原理图来说明。

![figure.1](https://pic.leetcode-cn.com/1617881719-yBaKKi-Insertion-sort-example-300px.gif)

## 代码
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def insertionSortList(self, head):
        """
        插入排序：除了第一个节点不动，第二个元素和前面已经排序好的元素进行比较，插入到合适的位置
        重复上述过程即可。
        比如:
            1 3 5 2 4   |左边为排序好的节点
            1 | 3 5 2 4
            1 3 | 5 2 4
            1 3 5 | 2 4
            1 2 3 5 | 4
            1 2 3 4 5 |
        :type head: ListNode
        :rtype: ListNode
        """
        if head.next is None:
            return head
        ends = head.next
        node = head.next
        start = head
        # 单独处理前两个节点
        if node.val < start.val:
            start.next = node.next
            node.next = start
            ends = start
            start = node
            head = node
        # 递归处理后面所有情况
        node = ends.next
        while node is not None:
            # 寻找合适的插入位置 (3种情况：头插入、中间插入、尾插入)
            # 头插入
            if node.val < start.val:
                ends.next = node.next
                node.next = start
                start = node
                head = node
                node = ends.next
            # 尾插入
            elif node.val > ends.val:
                ends = node
                node = ends.next
            # 中间插入
            else:
                cur = start
                # 寻找插入位置
                while True:
                    if node.val >= cur.val and node.val <=cur.next.val:
                        break
                    cur = cur.next
                # 插入
                ends.next = node.next
                node.next = cur.next
                cur.next = node
                node = ends.next
        return head
```