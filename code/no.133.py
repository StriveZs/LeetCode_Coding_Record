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