---
title: LeetCode No.25

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第二十五题
## 题目描述
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 
```
示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

 

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。
```

## 代码
## 超时的版本
分析愿原因为引入了统计长度的代码和两个多次循环重复
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        res = head
        length = 0
        # 计算长度
        while head != None:
            length += 1
            head = head.next
        if length < k:
            return head
        head = res
        part = int(length / k)  # 共有多少个整数组
        yushu = length % k # 余数
        num = 0
        NodeList = []
        # 使用栈
        while True:
            for i in range(k):
                NodeList.append(head)
                head = head.next
            for i in range(k):
                if i == 0 and num == 0:
                    res = NodeList.pop()
                    result = res
                else:
                    res.next = NodeList.pop()
                    res = res.next
            num += 1
            if num == part:
                if yushu != 0:
                    res.next = head
                break
        return result

if __name__ == '__main__':
    ln1 = ListNode(val=1)
    ln2 = ListNode(val=2)

    ln1.next = ln2

    s = Solution()
    print(s.reverseKGroup(ln1,2).val)
```

### 改正版本
去掉了一重循环，变成交换次序的操作了。  

```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = ListNode(val=0)
        current = head
        prev = dummy
        next = ListNode(val=0)
        dummy.next = head
        length = 0
        # 计算长度
        while head != None:
            length += 1
            head = head.next
        head = dummy.next  # 恢复head
        if length < k:
            return head
        part = int(length / k)  # 共有多少个整数组
        yushu = length % k # 余数
        for i in range(part):
            for j in range(k-1):
                next = current.next
                current.next = next.next
                next.next = prev.next
                prev.next = next
            prev = current
            current = prev.next

        return dummy.next

if __name__ == '__main__':
    ln1 = ListNode(val=1)
    ln2 = ListNode(val=2)

    ln1.next = ln2

    s = Solution()
    print(s.reverseKGroup(ln1,2).val)
```