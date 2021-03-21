---
title: LeetCode No.61

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第六十一题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个链表，旋转链表，将链表每个节点向右移动 k 个位置，其中 k 是非负数。
```
示例 1:

输入: 1->2->3->4->5->NULL, k = 2
输出: 4->5->1->2->3->NULL
解释:
向右旋转 1 步: 5->1->2->3->4->NULL
向右旋转 2 步: 4->5->1->2->3->NULL
示例 2:

输入: 0->1->2->NULL, k = 4
输出: 2->0->1->NULL
解释:
向右旋转 1 步: 2->0->1->NULL
向右旋转 2 步: 1->2->0->NULL
向右旋转 3 步: 0->1->2->NULL
向右旋转 4 步: 2->0->1->NULL
```

## 代码
```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
import copy
class Solution(object):
    def once_rotate(self,head):
        res = copy.copy(head) # 保存表头
        temp1 = head.val
        while head.next != None:
            temp = head.next.val
            head.next.val = temp1
            temp1 = temp
            head = head.next
        # 单独处理表尾
        res.val = temp1
        #print(res.val)
        return res

    def getLen(self,head):
        num = 1
        while head.next != None:
            head = head.next
            num += 1
        return num

    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode

        核心思想：
                实现一次链表移动，注意考虑尾部移动变成开头，注意考虑[]的情况
                然后调用上述操作k次

                上述操作超时，超时用例如下：
                    [1,2,3]
                    2000000000
                改进算法如下：
                1. 首先先遍历一遍列表得到列表的长度length
                2. 然后使用列表长度来对k进行取余，因为如果对于一个长度为3的序列，旋转3次等于没旋转
                3. 重复之前提到的链表 k%length 次
        """
        if head == None:
            return head
        length = self.getLen(head)
        #print(length)
        finlK = k % length
        for i in range(finlK):
            head = self.once_rotate(head)
            #print(head.val)
        return head

if __name__ == '__main__':
    head = ListNode(1)
    t1 = ListNode(2)
    t2 = ListNode(3)
    t3 = ListNode(4)
    t4 = ListNode(5)
    head.next=t1
    t1.next=t2
    t2.next = t3
    t3.next = t4
    t4.next = None
    s = Solution()
    res = s.rotateRight(head,2)
```