---
title: LeetCode No.160

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第160题—相交链表

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。如果两个链表没有交点，返回 null 。

图示两个链表在节点 c1 开始相交：

![figure.0](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_statement.png)

题目数据 保证 整个链式结构中不存在环。

注意，函数返回结果后，链表必须 保持其原始结构 。

 
```
示例 1：
```

![figure.1](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_1.png)

```
输入：intersectVal = 8, listA = [4,1,8,4,5], listB = [5,0,1,8,4,5], skipA = 2, skipB = 3
输出：Intersected at '8'
解释：相交节点的值为 8 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [4,1,8,4,5]，链表 B 为 [5,0,1,8,4,5]。
在 A 中，相交节点前有 2 个节点；在 B 中，相交节点前有 3 个节点。
示例 2：
```
![figure.2](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_2.png)
```
输入：intersectVal = 2, listA = [0,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
输出：Intersected at '2'
解释：相交节点的值为 2 （注意，如果两个链表相交则不能为 0）。
从各自的表头开始算起，链表 A 为 [0,9,1,2,4]，链表 B 为 [3,2,4]。
在 A 中，相交节点前有 3 个节点；在 B 中，相交节点前有 1 个节点。
示例 3：
```
![figure.3](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/14/160_example_3.png)
```
输入：intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
输出：null
解释：从各自的表头开始算起，链表 A 为 [2,6,4]，链表 B 为 [1,5]。
由于这两个链表不相交，所以 intersectVal 必须为 0，而 skipA 和 skipB 可以是任意值。
这两个链表不相交，因此返回 null 。
 

提示：

listA 中节点数目为 m
listB 中节点数目为 n
0 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA <= m
0 <= skipB <= n
如果 listA 和 listB 没有交点，intersectVal 为 0
如果 listA 和 listB 有交点，intersectVal == listA[skipA + 1] == listB[skipB + 1]

```

## 代码
```
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def timeout(self, headA, headB):
        """
        考虑用list分别分出两个head出现的节点, 然后遍历就好了 直到有首个重复的节点结束
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        listA = [] # 专门存储A的节点
        listB = [] # 专门存储B的节点
        while headA != None or headB != None:
            listA.append(headA)
            listB.append(headB)
            if headB in listA:
                return headB
            if headA in listB:
                return headA
            if headA != None:
                headA = headA.next
            if headB != None:
                headB = headB.next
        return None
    def getIntersectionNode(self, headA, headB):
        """
        参考了一下大佬的思路，由于两个链表长度不相同，但是可以使用另外一种办法让他们的长度变得一样长
        让两个head同时出发，如果其中一个head走到头了，则开始走另一个head的路，这样两条路长度就一样了，就会在同一个点相同，有点类似莫比乌斯环的感觉后面给图示
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        if headA is None or headB is None:
            return None
        # 开始走
        h1 = headA
        h2 = headB
        flag1 = True
        flag2 = True
        while h1 != h2:
            if h1 is not None:
                if h1.next is not None:
                    h1 = h1.next
                else:
                    if flag1:
                        h1 = headB
                        flag1 = False
                    else:
                        h1 = None
            if h2 is not None:
                if h2.next is not None:
                    h2 = h2.next
                else:
                    if flag2:
                        h2 = headA
                        flag2 = False
                    else:
                        h2 = None
        return h1

```