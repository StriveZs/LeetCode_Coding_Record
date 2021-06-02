class Solution(object):
    def one_chart_different(self, str1, str2):
        """
        判断输入的两个字符串是不是只有一个不一样, 默认输入的两个字符串长度相同
        :param str1: String
        :param str2: String
        :return: Boolean True/False
        """
        num = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                num += 1
            if num > 1:
                return False
        if num == 0:
            return False
        return True
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

    # fixme: BFS深度度优先搜索寻找最短路径 实质上就是暴力搜索  回溯法
    res_path = dict()
    min_dist = float('inf')
    def BFS_Search(self, start, ends, path, visited, adjacent_matrix):
        inf = float('inf')
        # 如果满足则存储路径和距离
        if start == ends:
            path_node = path.split(',')
            distance = len(path_node)
            if distance < self.min_dist:
                self.min_dist = distance
            if path not in self.res_path.keys():
                self.res_path[path] = distance
            return

        n = len(adjacent_matrix)
        for i in range(n):
            if adjacent_matrix[start][i] != inf and not visited[i]:
                t = path
                path = path + ',' + str(i)
                visited[i] = True
                self.BFS_Search(i, ends, path, visited, adjacent_matrix)
                path = t
                visited[i] = False


    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        根据给定的字典list构造一个图，考虑使用邻接矩阵构建一个图
        """
        inf = float('inf')
        if endWord not in wordList:
            return []
        if beginWord not in wordList:
            nodeList = [beginWord] + wordList  # 构造所有节点列表
        else:
            nodeList = wordList
        numList = [i for i in range(len(nodeList))] # 构造每个节点对应的数字状态
        node_num_dict = dict(zip(nodeList,numList)) # 构建对应关系的字典
        num_node_dict = dict(zip(numList,nodeList)) # 构造反向对应关系
        adjacent_matrix = [[inf for _ in range(len(nodeList))] for _ in range(len(nodeList))] # 邻接矩阵
        # 构建邻接矩阵
        for i in nodeList:
            for j in nodeList:
                if i != j:
                    if len(i) == len(j):
                        if self.one_chart_different(i,j):
                            adjacent_matrix[node_num_dict[i]][node_num_dict[j]] = 1
                            adjacent_matrix[node_num_dict[j]][node_num_dict[i]] = 1
        #print(adjacent_matrix)
        # 使用迪杰斯特拉算法
        # distance, path = self.Dijkstra(0,adjacent_matrix)
        # resList = path[-1].split(',')
        # res = []
        # if len(resList) != 0:
        #     res.append(num_node_dict[0])
        # for i in resList:
        #     res.append(num_node_dict[int(i)])
        # return res
        # 使用BFS回溯法搜索
        visited = [False] * len(adjacent_matrix)
        visited[0] = True
        self.BFS_Search(nodeList.index(beginWord),nodeList.index(endWord),str(nodeList.index(beginWord)),visited,adjacent_matrix)
        res = []
        for item in self.res_path.keys():
            if self.res_path[item] == self.min_dist:
                temp = []
                path = item.split(',')
                for i in range(len(path)):
                    temp.append(num_node_dict[int(path[i])])
                res.append(temp)
        return res


if __name__ == '__main__':
    s = Solution()
    print(s.findLadders(beginWord = "hot", endWord = "dog", wordList = ["hot","dog","dot"]))