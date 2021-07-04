---
title: LeetCode No.138

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第138题—复制带随机指针的链表
今天获得了习近平七年知青岁月这本书，很开心！

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个长度为 n 的链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。

构造这个链表的 深拷贝。 深拷贝应该正好由 n 个 全新 节点组成，其中每个新节点的值都设为其对应的原节点的值。新节点的 next 指针和 random 指针也都应指向复制链表中的新节点，并使原链表和复制链表中的这些指针能够表示相同的链表状态。复制链表中的指针都不应指向原链表中的节点 。

例如，如果原链表中有 X 和 Y 两个节点，其中 X.random --> Y 。那么在复制链表中对应的两个节点 x 和 y ，同样有 x.random --> y 。

返回复制链表的头节点。

用一个由 n 个节点组成的链表来表示输入/输出中的链表。每个节点用一个 [val, random_index] 表示：

val：一个表示 Node.val 的整数。
random_index：随机指针指向的节点索引（范围从 0 到 n-1）；如果不指向任何节点，则为  null 。
你的代码 只 接受原链表的头节点 head 作为传入参数。

![figure.1](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e1.png)

```
示例 1：

输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
```

![figure.2](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e2.png)

```
示例 2：

输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
```
![figure.3](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/01/09/e3.png)
```
示例 3：

输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

0 <= n <= 1000
-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
```

## 代码
### Python取巧方法（不建议！！！）
如果是生活中可以用库，真正OJ不建议使用。
```
return copy.deepcopy(head)
```
### 实打实的哈希方法
```
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution(object):
    def copyRandomList(self, head):
        """
        题目分析：
            实质上就是链表的深度copy，同时要保留链表之间的random连接关系

            比较困难的一点就是: 如何找到random对应的节点关系

            想法：
                因为random_index是对应的节点索引，因此考虑先不设置random关系来构建一个完全相同的链表，并将节点对应的索引构建一个MAP和索引对应的节点构建一个MAP
                然后根据原来链表的random_index来构建索引关系
            构建：
                1. 旧链表：节点到index的映射
                2. 新链表：index到节点的映射
            第一遍遍历先构建一个全新的链表
            第二遍遍历在根据哈希关系构建random关系
        :type head: Node
        :rtype: Node
        """
        if head is None:
            return None
        index_node_dict = dict() # 新链表的index和节点对应关系
        node_index_dict = dict() # 旧链表的节点和index对应关系
        start = head
        new_head = Node(head.val)
        new_start = new_head
        index_node_dict[0] = new_head
        node_index_dict[head] = 0
        # 构建一个新的链表
        num = 1
        while start.next != None:
            start = start.next
            node = Node(start.val)
            new_start.next = node
            new_start = node
            index_node_dict[num] = node
            node_index_dict[start] = num
            num += 1
        # 构建random关系
        start = head
        new_start = new_head
        while start != None:
            # 单独处理为NULL情况
            if start.random is None:
                new_start.random = None
            else:
                new_start.random = index_node_dict[node_index_dict[start.random]] # random是按照index索引的
            start = start.next
            new_start = new_start.next

        return new_head

```