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
    # fixme: 使用BFS进行广度优先搜索
    def BFS_memory_search(self, start, end_num, adjacent_matrix):
        """
        使用带有记忆的BFS来进行搜索，层数逐渐增加就可以了，直到最先扩展到最终节点就结束
        有点类似树扩展的方法,用字典来记录深度
        :param start: Int 给点初始节点在邻接矩阵中的下标
        :param end_num: 终止节点
        :param adjacent_matrix: 邻接矩阵
        :return: distance, path 返回距离和路径
        """
        inf = float('inf')
        # 初始化操作
        depth_dict = {} # 记忆深度词典
        depth_dict[start] = 1 # 初始化
        quene = [] # 队列
        quene.append(start)
        n = len(adjacent_matrix) # 节点个数
        step = None
        for i in range(1,n):
            if len(quene) == 0:
                return step
            node = quene.pop(0) # 队首出列
            for j in range(n):
                if adjacent_matrix[node][j] != inf and j not in depth_dict.keys(): # 证明可以扩展
                    quene.append(j) # 入队
                    depth_dict[j] = depth_dict[node] + 1 # 深度记录
                if j == end_num and end_num in depth_dict.keys():
                    step = depth_dict[j]
                    return step
        return step

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        根据给定的字典list构造一个图，考虑使用邻接矩阵构建一个图
        """
        inf = float('inf')
        if endWord not in wordList:
            return 0
        if beginWord not in wordList:
            nodeList = [beginWord] + wordList  # 构造所有节点列表
        else:
            nodeList = wordList
            nodeList.remove(nodeList[nodeList.index(beginWord)])
            nodeList = [beginWord] + wordList # 将初始节点至为第一个
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
        step = self.BFS_memory_search(0,nodeList.index(endWord),adjacent_matrix)
        if step == None:
            return 0
        return step

    def new_version(self, beginWord, endWord, wordList):
        quene = []
        quene.append(beginWord)
        step = 0
        while len(quene) != 0:
            step += 1
            sz = len(quene)
            while sz > 0:
                hope = quene.pop(0)
                if hope == endWord:
                    return step

                # 对每个word进行判断
                for i in range(len(wordList)):
                    if len(wordList[i]) == 0 or len(wordList[i]) != len(beginWord):
                        continue
                    # 判断差异性
                    if self.one_chart_different(hope,wordList[i]):
                        quene.append(wordList[i])
                        wordList[i] = ""
                sz -= 1
        return 0

    def ladderLength_advance(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0

        l = len(endWord)

        ws = set(wordList)

        head = {beginWord}
        tail = {endWord}
        tmp = list('abcdefghijklmnopqrstuvwxyz')
        res = 1
        while head:
            if len(head) > len(tail):
                head, tail = tail, head

            q = set()
            for cur in head:
                for i in range(l):
                    for j in tmp:
                        word = cur[:i] + j + cur[i + 1:]

                        if word in tail:
                            return res + 1

                        if word in ws:
                            q.add(word)
                            ws.remove(word)
            head = q
            res += 1

        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.ladderLength_advance(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))