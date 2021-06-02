---
title: LeetCode No.126

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第126题—单词接龙II
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：

每对相邻的单词之间仅有单个字母不同。
转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
sk == endWord
给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。

```

示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
解释：存在 2 种最短的转换序列：
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：[]
解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
 

提示：

1 <= beginWord.length <= 7
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有单词 互不相同
```
## 解题思路

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/IMG_0713.PNG)

## 代码
回溯法做的. 不知道为什么，我写的代码，一个测试用例提交报错，我同样在本地测试一点问题都没有。不知道啥情况了，代码整体思想没有问题。

```
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
```