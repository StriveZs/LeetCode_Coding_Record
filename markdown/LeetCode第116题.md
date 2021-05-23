---
title: LeetCode No.116

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第116题—填充每个节点的下一个右侧节点指针
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个 完美二叉树 ，其所有叶子节点都在同一层，每个父节点都有两个子节点。二叉树定义如下：
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
 
![figure.1](https://assets.leetcode.com/uploads/2019/02/14/116_sample.png)

```
示例：

输入：root = [1,2,3,4,5,6,7]
输出：[1,#,2,3,#,4,5,6,7,#]
解释：给定二叉树如图 A 所示，你的函数应该填充它的每个 next 指针，以指向其下一个右侧节点，如图 B 所示。序列化的输出按层序遍历排列，同一层节点由 next 指针连接，'#' 标志着每一层的结束。
 
提示：

树中节点的数量少于 4096
-1000 <= node.val <= 1000
```

## 代码
采用带记忆的前序遍历即可。
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
            完美二叉树：它的所有叶子节点都在同一层，每个父结点都有两个叶子结点

            类似DFS的感觉，将节点分层，一层的都添加到一个队列中。
            可以考虑设置深度，将一个深度的放在同一个列表中，构建深度字典
        """
        depth_dict = dict() # 深度词典初始化
        self.bfs(root,0)
        return root


```