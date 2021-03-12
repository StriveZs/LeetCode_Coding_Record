---
title: LeetCode No.52

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第五十二题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Folk :)
## 题目描述
n 皇后问题 研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。

给你一个整数 n ，返回 n 皇后问题 不同的解决方案的数量。

![figure.1](https://assets.leetcode.com/uploads/2020/11/13/queens.jpg)

```
示例 1：

输入：n = 4
输出：2
解释：如上图所示，4 皇后问题存在两个不同的解法。
示例 2：

输入：n = 1
输出：1
 

提示：

1 <= n <= 9
皇后彼此不能相互攻击，也就是说：任何两个皇后都不能处于同一条横行、纵行或斜线上。
```

## 代码
仅对上一个代码进行简单的修改，即可以得到本题对应的代码。  

```
class Solution(object):
    def judge(self,QiPan, placeI, placeJ, n):
        """
        :arg 判断新位置的皇后是否合法
        :type QiPan: List[List[str]]
        :type placeI: int
        :type placeJ: int
        :type n: int
        :rtype : Boolean
        """
        # 剪枝判断法： 由于给定当前i和j，又因为是从左上往右下依次放置皇后的，因此不需要判断行数和列数同时大于当前位置的元素
        flag = True
        for i in range(n):
            for j in range(n):
                # 去掉还没有放置皇后的位置
                if i > placeI and j > placeJ:
                    continue
                # 判断和n在同一行上的位置
                if i == placeI:
                    if QiPan[i][j] == 'Q':
                        flag = False
                        return flag
                # 判断和n在同一列上的位置
                if j == placeJ:
                    if QiPan[i][j] == 'Q':
                        flag = False
                        return flag

                # 判断斜线上的位置, 可以用过计算斜率来确定是否在一条斜线上
                if i != placeI and j != placeJ:
                    if abs(i - placeI)/abs(j - placeJ) == 1:
                        if QiPan[i][j] == 'Q':
                            flag = False
                            return flag
        return flag

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        核心思想：
                首先想到的是回溯法，通过回溯法来遍历所有的可能，如果满足条件则选择该情况，否则撤回选择
                def backtrack(path, selected):
                    if 满足停止条件：
                        res.append(path)
                    for 选择 in 选择列表：
                        做出选择
                        递归执行backtrack
                            满足则return True
                        如果不满足要求就撤销选择
        """
        QiPan = []
        for i in range(n):
            QiPan.append(['.' for i in range(n)])
        # print(QiPan)

        res = [] # 存储结果棋盘

        def backtrack(QiPan, i, n):
            """
            :arg 回溯法
            :type QiPan: List[List[str]]
            :type i: int
            :type n: int
            """
            # 停止条件
            if i == n:
                import copy
                temp = copy.deepcopy(QiPan)
                once_res = []
                # 处理一下结果
                for m in range(len(temp)):
                    str1 = ""
                    for n in range(len(temp[m])):
                        str1 += temp[m][n]
                    once_res.append(str1)
                res.append(once_res)
                return
            # 遍历所有选择
            for j in range(n):
                # 进行选择
                if self.judge(QiPan,i,j,n):
                    QiPan[i][j] = 'Q'
                    backtrack(QiPan,i+1,n)
                    QiPan[i][j] = '.'  # 撤销选择

        backtrack(QiPan,0,n)

        return len(res)

if __name__ == '__main__':
    s = Solution()
    print(s.totalNQueens(1))


```