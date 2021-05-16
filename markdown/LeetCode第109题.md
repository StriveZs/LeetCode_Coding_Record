---
title: LeetCode No.109

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第109题—将有序链表转换为二叉搜索树
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个单链表，其中的元素按升序排序，将其转换为高度平衡的二叉搜索树。

本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
```
示例:

给定的有序链表： [-10, -3, 0, 5, 9],

一个可能的答案是：[0, -3, 9, -10, null, 5], 它可以表示下面这个高度平衡二叉搜索树：

      0
     / \
   -3   9
   /   /
 -10  5
```
## 代码
两种办法，一种是非常蠢直接转换，但是十分不推荐，另一种是使用快慢指针寻找链表的中间节点的方法。

```
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution(object):
    res = []
    def balancedBST(self,partNode):
        """
            我们需要将中间的节点作为根节点，这样就划分成一个分而治之的问题了
            分治思想：每个划分的部分都是以中间节点作为当前子树的根节点
        """
        if len(partNode) == 1:
            return TreeNode(partNode[0])
        middle = int(len(partNode)/2)
        node = TreeNode(partNode[middle])
        node.left = self.balancedBST(partNode[0:middle])
        if middle == len(partNode)-1:
            node.right = None
        else:
            node.right = self.balancedBST(partNode[middle+1:])
        return node
    def nodeList2SortedList(self,node):
        """
            递归得到有序列表
        """
        if node != None:
            self.res.append(node.val)
            self.nodeList2SortedList(node.next)

    def fastSlowPointer(self,head):
        """
            快慢指针寻找链表中点，快指针走两步，慢指针走一步，这样当快指针走到结束时，就可以很容易的找到链表的中点
        """
        if head == None:
            return None
        if head.next == None: # 下一个节点为null
            return TreeNode(head.val)
        # 快慢指针寻找中间节点
        fastPointer = head
        slowPointer = head
        pre = None # 用于划分左右子树
        while fastPointer != None and fastPointer.next != None:
            fastPointer = fastPointer.next.next
            pre = slowPointer # 最终得到中间节点的前一个节点，用于划分左右子树
            slowPointer = slowPointer.next
        pre.next = None # 分割链表
        # 构造树以及左右子树
        middleNode = TreeNode(slowPointer.val)
        middleNode.left = self.fastSlowPointer(head) # 左子树
        middleNode.right = self.fastSlowPointer(slowPointer.next)
        return middleNode

    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        核心思想：
            高度平衡的二叉树：每个节点的左右子树的高度差绝对值不超过1
            而且有要求是二叉搜索树，因此中序遍历要是升序

            类似上一道题，这里我想一个比较蠢的办法就是将有序链表先转换为有序数组
            然后在使用108题的方法，将有序数组转换为二叉搜索树

            还有一个办法就是按照上一题的操作，只不过从计算列表中点，变成了找列表的中点
        """
        if head == None:
            return None
        self.res = []
        self.nodeList2SortedList(head)
        return self.balancedBST(self.res)
    def sortedListToBSTNewVersion(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        核心思想：
            高度平衡的二叉树：每个节点的左右子树的高度差绝对值不超过1
            而且有要求是二叉搜索树，因此中序遍历要是升序

            类似上一道题，这里我想一个比较蠢的办法就是将有序链表先转换为有序数组
            然后在使用108题的方法，将有序数组转换为二叉搜索树

            还有一个办法就是按照上一题的操作，只不过从计算列表中点，变成了找列表的中点
        """
        return self.fastSlowPointer(head)
```