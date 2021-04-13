---
title: LeetCode No.83

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第八十三题—删除排序链表中的重复元素
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
不明白为什么这道题放在83，上一题放在82，基本上就是魔改一下。  

存在一个按升序排列的链表，给你这个链表的头节点 head ，请你删除所有重复的元素，使每个元素 只出现一次 。

返回同样按升序排列的结果链表。

![figure.1](https://assets.leetcode.com/uploads/2021/01/04/list1.jpg)
 
```
示例 1：

输入：head = [1,1,2]
输出：[1,2]
```

![figure.2](https://assets.leetcode.com/uploads/2021/01/04/list2.jpg)

```
示例 2：

输入：head = [1,1,2,3,3]
输出：[1,2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序排列
```

## 代码
### 冗余版本(AC了)
```
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        核心思想：
                这道题排在上一道题后面我是没想到的
                直接拿上一道题的来改就好了
                就是上一道题的第一部分
        """
        # 处理全为空的情况
        if head == None:
            return head
        # 单独处理只有一个结点的情况
        if head.next == None:
            return head
        listNode = [] # 记录元素
        listNode.append(head.val)
        temp = head.next
        pre = head  # 记录前一个结点, 方便执行删除操作
        while temp != None: # 这个约束保证了最少有两个结点，对于一个结点直接返回就好了
            if temp.val in listNode:
                pre.next = temp.next # 删除中间的结点
            else:
                listNode.append(temp.val) # 如果不在listNode中则添加进入
                pre = temp # 前指针向后移动一个
            temp = temp.next  # 指针指向下一个节点
        return head
```

### 优化版本
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode

        核心思想：
                这道题排在上一道题后面我是没想到的
                直接拿上一道题的来改就好了
                就是上一道题的第一部分
        """
        temp = head
        while temp != None and temp.next != None:
            if temp.val == temp.next.val: # 重复元素
                temp.next = temp.next.next # 删除
            else:
                temp = temp.next
        return head
```