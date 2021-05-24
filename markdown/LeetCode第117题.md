---
title: LeetCode No.117

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第117题—填充每个节点的下一个右侧节点指针II
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个二叉树
```
struct Node {
  int val;
  Node *left;
  Node *right;
  Node *next;
}
填充它的每个 next 指针，让这个指针指向其下一个右侧节点。如果找不到下一个右侧节点，则将 next 指针设置为 NULL。

初始状态下，所有 next 指针都被设置为 NULL。

进阶：

你只能使用常量级额外空间。
使用递归解题也符合要求，本题中递归程序占用的栈空间不算做额外的空间复杂度。
```

![figure.1](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/02/15/117_sample.png)


```
示例：

输入：root = [1,2,3,4,5,null,7]
输出：[1,#,2,3,#,4,5,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化输出按层序遍历顺序（由 next 指针连接），'#' 表示每层的末尾。
 

提示：

树中的节点数小于 6000
-100 <= node.val <= 100
```

## 代码
```
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution(object):
    depth_dict = dict() # 深度字典
    # fixme:采用bfs添加深度，将相同的深度放在同一个列表中
    def bfs(self, node, depth):
        """
        采用前序遍历
        :param node: Node
        :param depth: Int 深度
        :return:
        """
        if node == None:
            return
        # 创建深度层次
        if depth not in self.depth_dict.keys():
            self.depth_dict[depth] = list()
        # 处理在同一深度的节点
        else:
            # 带记忆的处理方式，将链尾的值指向下一个同深度的节点
            self.depth_dict[depth][-1].next = node
        self.depth_dict[depth].append(node) # 将结点存进去
        self.bfs(node.left,depth+1)
        self.bfs(node.right,depth+1)

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        核心思想:
            和前面一题的代码一毛一样

            类似DFS的感觉，将节点分层，一层的都添加到一个队列中。
            可以考虑设置深度，将一个深度的放在同一个列表中，构建深度字典
        """
        depth_dict = dict() # 深度词典初始化
        self.bfs(root,0)
        return root


```