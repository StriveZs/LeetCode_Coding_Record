---
title: LeetCode No.148

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第148题—链表排序

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

进阶：

你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？

![figure,1](https://assets.leetcode.com/uploads/2020/09/14/sort_list_1.jpg)
```
示例 1：

输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：
```
![figure,2](https://assets.leetcode.com/uploads/2020/09/14/sort_list_2.jpg)
```
输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105
```

## 归并排序思想
用一张图来说明归并排序:

![figure.3](https://gitee.com/zyp521/upload_image/raw/master/wWJB4K.jpg)

## 代码
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    # fixme: 归并排序(自底向上合并链表)
    def merge(self, node1, node2):
        dummy = ListNode()
        pre = dummy
        while node1 is not None and node2 is not None:
            if node1.val <= node2.val:
                pre.next = node1
                pre = pre.next
                node1 = node1.next
            else:
                pre.next = node2
                pre = pre.next
                node2 = node2.next
        if node1 is not None:
            pre.next = node1
        if node2 is not None:
            pre.next = node2
        return dummy.next

    # fixme: 归并排序(自顶向下划分链表)
    def merge_sort(self, head):
        if head is None or head.next is None:
            return head
        # 快慢指针寻找中间节点
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        # 找到中间节点之后断开链表
        new_head = slow.next
        slow.next = None
        # 递归断开所有的节点
        slow = self.merge_sort(head)
        fast  =self.merge_sort(new_head)

        # 合并
        return self.merge(slow, fast)

    def sortList(self, head):
        """
        参考大佬的题解考虑使用归并排序
        对于数组的归并排序来说，可以直接根据数组的长度来找到中间值，对于链表来说，我们可以通过快慢指针来找到中间节点
        然后采用递归的方法将链表层层断开，排序后
        最后再合并
        :type head: ListNode
        :rtype: ListNode
        """
        return self.merge_sort(head)
```