---
title: LeetCode No.143

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第143题—重排链表
即将回家！

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个单链表 L：L0→L1→…→Ln-1→Ln ，
将其重新排列后变为： L0→Ln→L1→Ln-1→L2→Ln-2→…

你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。
```
示例 1:

给定链表 1->2->3->4, 重新排列为 1->4->2->3.
示例 2:

给定链表 1->2->3->4->5, 重新排列为 1->5->2->4->3.
```
## 代码
```
import copy
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reorderList(self, head):
        """
        分析题目可以得到这个链表就是通过中间节点划分之后，前端链表和后端链表合并的结果
        因此可以先用快慢指针来找到中间节点，然后用栈存储后端链表节点
        最后实现前端链表和栈节点合并即可
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        if head is None or head.next is None:
            return head
        fast = head # 快指针
        slow = head # 慢指针
        mid = None # 中间节点
        forward = [] # 用于存储前向链表的队列
        stack = [] # 用于存储后端链表的栈
        # 快慢指针寻找中间节点
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            forward.append(slow)
            slow = slow.next
            mid = slow
        # 遍历后端链表节点，将所有节点都放到栈里面
        node = mid
        while node is not None:
            stack.append(node)
            node = node.next
        # 合并前端链表和反向后端链表
        node = head
        temp = stack[-1]
        stack.pop()
        node.next = temp
        node = node.next
        for i in range(1,len(forward)):
            node.next = forward[i]
            node = node.next
            temp = stack[-1]
            stack.pop()
            node.next = temp
            node = node.next
        if len(stack) != 0:
            node.next = stack[-1]
            node = node.next
        node.next = None

        return head

if __name__ == '__main__':
    root = ListNode(1)
    node1 = ListNode(2)
    node2 = ListNode(3)
    node3 = ListNode(4)

    root.next = node1
    node1.next = node2
    node2.next = node3

    s = Solution()
    t =  s.reorderList(root)
    while t is not None:
        print(t.val)
        t = t.next

```