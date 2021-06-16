---
title: LeetCode No.133

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第133题—克隆图

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你无向 连通 图中一个节点的引用，请你返回该图的 深拷贝（克隆）。

图中的每个节点都包含它的值 val（int） 和其邻居的列表（list[Node]）。

class Node {
    public int val;
    public List<Node> neighbors;
}
 

测试用例格式：

简单起见，每个节点的值都和它的索引相同。例如，第一个节点值为 1（val = 1），第二个节点值为 2（val = 2），以此类推。该图在测试用例中使用邻接列表表示。

邻接列表 是用于表示有限图的无序列表的集合。每个列表都描述了图中节点的邻居集。

给定节点将始终是图中的第一个节点（值为 1）。你必须将 给定节点的拷贝 作为对克隆图的引用返回。

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/8GP8e1.jpg)

``` 

示例 1：

输入：adjList = [[2,4],[1,3],[2,4],[1,3]]
输出：[[2,4],[1,3],[2,4],[1,3]]
解释：
图中有 4 个节点。
节点 1 的值是 1，它有两个邻居：节点 2 和 4 。
节点 2 的值是 2，它有两个邻居：节点 1 和 3 。
节点 3 的值是 3，它有两个邻居：节点 2 和 4 。
节点 4 的值是 4，它有两个邻居：节点 1 和 3 。
```

![figure.2](https://gitee.com/zyp521/upload_image/raw/master/u922LX.jpg)

```
示例 2：

输入：adjList = [[]]
输出：[[]]
解释：输入包含一个空列表。该图仅仅只有一个值为 1 的节点，它没有任何邻居。
示例 3：

输入：adjList = []
输出：[]
解释：这个图是空的，它不含任何节点。
```

![figure.3](https://gitee.com/zyp521/upload_image/raw/master/iaX0Mu.jpg)

```
示例 4：

输入：adjList = [[2],[1]]
输出：[[2],[1]]
 
提示：

节点数不超过 100 。
每个节点值 Node.val 都是唯一的，1 <= Node.val <= 100。
无向图是一个简单图，这意味着图中没有重复的边，也没有自环。
由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居。
图是连通图，你可以从给定节点访问到所有节点。
```
## 代码
好奇挖，自己写的命名逻辑一点问题都没有，硬是不接受！！！

```
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution(object):
    node_neighbors_relation_dict = dict()
    val_node = dict()
    # fixme:DFS建图
    def dfs(self, node):
        if node.val not in self.node_neighbors_relation_dict.keys():
            if node.val not in self.val_node.keys():
                self.val_node[node.val] = Node(node.val)
            self.node_neighbors_relation_dict[node.val] = []
            if len(node.neighbors) != 0:
                for item in node.neighbors:
                    self.node_neighbors_relation_dict[node.val].append(item.val)
                    self.dfs(item)
        return

    def error(self, node):
        """
        :type node: Node
        :rtype: Node
        几个前提条件:
            1. 每个节点值 Node.val 都是唯一的，利用这一点就可以建立一个访问过节点的列表，保证不会再次被访问
            2. 图是连通图，你可以从给定节点访问到所有节点
            3. 由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居
        然后采用深度DFS形成邻居关系字典，其实这里考虑使用邻接矩阵或者邻接表也可以
        然后最后再利用字典关系进行建图
        """
        self.node_neighbors_relation_dict = dict()
        self.val_node = dict()
        if node == None:
            return None
        self.dfs(node)
        # 利用构建的节点邻居关系字典来建图
        res = None
        num = 1
        for item in self.node_neighbors_relation_dict.keys():
            temp = Node(item)
            if num == 1:
                res = temp
                num +=1
            for iNode in self.node_neighbors_relation_dict[item]:
                temp.neighbors.append(self.val_node[iNode])
        return res
    res = dict()
    # fixme:上一个版本出问题了，下面是修正版本，虽然没找出来什么问题
    def DFS_NV(self, node):
        self.res[node] = Node(node.val) # 新建节点
        for iNode in node.neighbors:
            if iNode not in self.res.keys():
                self.res[node].neighbors = [self.DFS_NV(iNode)]
            else:
                self.res[node].neighbors = [self.res[iNode]]
        return self.res[node]

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        几个前提条件:
            1. 每个节点值 Node.val 都是唯一的，利用这一点就可以建立一个访问过节点的列表，保证不会再次被访问
            2. 图是连通图，你可以从给定节点访问到所有节点
            3. 由于图是无向的，如果节点 p 是节点 q 的邻居，那么节点 q 也必须是节点 p 的邻居
        然后采用深度DFS形成邻居关系字典，其实这里考虑使用邻接矩阵或者邻接表也可以
        然后最后再利用字典关系进行建图
        """
        if node == None:
            return node
        self.res = dict()
        return self.DFS_NV(node)


if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node1.neighbors.append(node2)
    node1.neighbors.append(node4)
    node2.neighbors.append(node1)
    node2.neighbors.append(node3)
    node3.neighbors.append(node2)
    node3.neighbors.append(node4)
    node4.neighbors.append(node1)
    node4.neighbors.append(node3)
    s = Solution()
    print(s.cloneGraph(node1).val)
```