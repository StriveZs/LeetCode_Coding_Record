---
title: LeetCode 基于邻接矩阵的Dijkstra算法

categories:
  - 算法

tags:
  - Programing
  - 算法
  - 图
  - 最短路径
  - Dijkstra
---

# 基于邻接矩阵的Dijkstra算法
如果你的图不是邻接矩阵，转换成矩阵的形式就可以了。这里节点我就是用index表示的。  

```
# fixme: Dijkstra算法寻找最短路径，从给定初始点到每个节点的最短路径
    def Dijkstra(self, start, adjacent_matrix):
        """
        :param start: Int 给点初始节点在邻接矩阵中的下标
        :param adjacent_matrix: 邻接矩阵
        :return: distance, path 返回到每个节点的最短距离，返回路径
        """
        # 初始化操作
        n = len(adjacent_matrix) # 节点个数
        inf = float('inf')
        distance = [inf] * n # 用于存放从某个点到其他点的最短路径长度
        path = [None] * n # 用于存放从初始点到其他点的路径
        final = [None] * n # 用于存放从初始点到其他点的最短路径
        for i in range(n):
            final[i] = False
            distance[i] = adjacent_matrix[start][i]
            path[i] = ""  # 路径置空
            if distance[i] < inf:
                path[i] = str(i)
        distance[start] = 0
        final[start] = True
        # 算法
        for i in range(1,n):
            min = inf
            for k in range(n):
                if not final[k] and distance[k] < min:
                    v = k
                    min = distance[k]
            final[v] = True
            for k in range(n):
                if not final[k] and min + adjacent_matrix[v][k] < distance[k]:
                    distance[k] = min + adjacent_matrix[v][k]
                    path[k] = path[v] + ',' + str(k)
        return distance, path
```