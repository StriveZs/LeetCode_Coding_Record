---
title: LeetCode No.92

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第九十二题—反转链表II
## 题目描述
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 
![figure.1](https://assets.leetcode.com/uploads/2021/02/19/rev2ex2.jpg)

```
示例 1：

输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]
 
提示：

链表中节点数目为 n
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n
```

## 代码
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode

            核心思想：
                    使用一个额外的链表来存储翻转后的结果
                    对于原链表沿分别记录需要反转部分前后的node
        """
        # 处理特殊情况
        if left == right:
            return head
        # 反转部分前后的Node
        leftPart = ListNode()
        rightPart = ListNode()

        # 新出链表存储反转后的结果
        newHead = ListNode()
        last = ListNode()

        num = 0 # 计数菌
        temp = head # 访问Node
        flag = True
        while temp != None and flag:
            num += 1
            # 记录左右边界
            if num == left-1:
                leftPart = temp
            if num == right+1:
                rightPart = temp
                flag = False # 结束标志
            # 反转
            if num >= left and num <= right:
                tt = ListNode(val=temp.val)
                tt.next = newHead.next
                newHead.next = tt
                if num == left:
                    last = tt # 记录尾结点
                    # print('---' + str(last.val))
            temp = temp.next
        # 单独处理头尾反转特殊情况
        if left == 1 and num==right:
            return newHead.next
        elif left == 1:
            last.next = rightPart  # 右边连接
            return newHead.next
        elif num == right:
            leftPart.next = newHead.next  # 左边连接
            return head

        # 链表链接
        leftPart.next = newHead.next # 左边连接
        last.next = rightPart  # 右边连接
        return head

if __name__ == '__main__':
    a1 = ListNode(3)
    a2 = ListNode(5)

    a1.next = a2

    s = Solution()
    head = s.reverseBetween(a1,1,2)
    while head != None:
        print(str(head.val)+' ')
        head = head.next
```