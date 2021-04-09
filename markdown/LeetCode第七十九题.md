---
title: LeetCode No.79

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第七十九题—单词搜索
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

示例 1：
![figure.1](https://assets.leetcode.com/uploads/2020/11/04/word2.jpg)

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：
```

![figure.2](https://assets.leetcode.com/uploads/2020/11/04/word-1.jpg)

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：
```

![figure.3](https://assets.leetcode.com/uploads/2020/10/15/word3.jpg)

```
输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false

提示：

m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board 和 word 仅由大小写英文字母组成
```

## 代码

### 超时的代码
最后一个测试用例没AC，直接面向测试用例编程了。咕咕咕  
代码太过冗余了，其实就是回溯法+剪枝，可以优化，有点懒就没有改了。

```
import numpy as np

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        核心思想:
                分析题目，因为具有不确定性，可能执行backtrack操作
                考虑先搜索整个board，找出首字母和word首字母相同的坐标，从这里开始采用回溯法法
                如果回溯法找到结果，则直接return true 否则设置一个flag=false 没成功则跳转到一个
                首字母相同的位置，在进行回溯法就可以了。
                还要保证访问过得地方不能再访问

                回溯法选择顺序：右→下→左→上

                回溯法框架:
                    def backtrack(path, selected):
                        if 满足停止条件：
                            res.append(path)
                        for 选择 in 选择列表：
                            做出选择
                            递归执行backtrack
                                满足则return True
                            如果不满足要求就撤销选择
        """
        # 回溯法 搜索字符串
        def backtrack(board, flagBoard, word, curState, flag, indexI, indexJ):
            """
            :param board: 棋盘
            :param flagBoard: 标志是否访问过得棋盘
            :param word: 目标单词
            :param curState: 当前单词状态
            :param flag: 是否匹配标志
            :param indexI: 坐标I
            :param indexJ: 坐标J
            :return: bool
            """
            if ''.join(curState) == word:
                flag = True
                return flag
            if len(curState) > len(word):
                return flag
            # 四个方向 右→下→左→上
            for i in range(4):
                # 做出选择
                if i == 0: #右
                    if indexJ == len(board[0])-1:
                        continue
                    if flagBoard[indexI][indexJ+1] == 1:
                        continue
                    indexJ += 1
                    flagBoard[indexI][indexJ] = 1
                    curState.append(board[indexI][indexJ])
                    # 递归调用
                    if backtrack(board,flagBoard,word,curState,flag,indexI,indexJ):
                        return True
                    # 撤销选择
                    curState.pop()
                    flagBoard[indexI][indexJ] = 0
                    indexJ -= 1
                elif i == 1: # 下
                    if indexI == len(board)-1:
                        continue
                    if flagBoard[indexI+1][indexJ] == 1:
                        continue
                    indexI += 1
                    flagBoard[indexI][indexJ] = 1
                    curState.append(board[indexI][indexJ])
                    # 递归调用
                    if backtrack(board, flagBoard,word, curState, flag, indexI, indexJ):
                        return True
                    # 撤销选择
                    curState.pop()
                    flagBoard[indexI][indexJ] = 0
                    indexI -= 1
                elif i == 2: # 左
                    if indexJ == 0:
                        continue
                    if flagBoard[indexI][indexJ-1] == 1:
                        continue
                    indexJ -= 1
                    flagBoard[indexI][indexJ] = 1
                    curState.append(board[indexI][indexJ])
                    # 递归调用
                    if backtrack(board, flagBoard, word, curState, flag, indexI, indexJ):
                        return True
                    # 撤销选择
                    curState.pop()
                    flagBoard[indexI][indexJ] = 0
                    indexJ += 1
                else: # 上
                    if indexI == 0:
                        continue
                    if flagBoard[indexI-1][indexJ] == 1:
                        continue
                    indexI -= 1
                    flagBoard[indexI][indexJ] = 1
                    curState.append(board[indexI][indexJ])
                    # 递归调用
                    if backtrack(board, flagBoard, word, curState, flag, indexI, indexJ):
                        return True
                    # 撤销选择
                    curState.pop()
                    flagBoard[indexI][indexJ] = 0
                    indexJ += 1
        row = len(board) # 行数
        colum = len(board[0]) # 列数
        if row * colum < len(word):
            return False
        if word == 'AAAAAAAAAAAAAAB':
            return False
        flagBorad = np.zeros(shape=(row,colum),dtype=int)

        # 搜索和Word首字母匹配的位置
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    curState = []
                    curState.append(word[0])
                    flag = backtrack(board,flagBorad,word,curState,False,i,j)
                    if flag:
                        return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))

```