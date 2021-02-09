---
title: LeetCode No.36

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第三十六题

## 题目描述
判断一个 9x9 的数独是否有效。只需要根据以下规则，验证已经填入的数字是否有效即可。

数字 1-9 在每一行只能出现一次。
数字 1-9 在每一列只能出现一次。
数字 1-9 在每一个以粗实线分隔的 3x3 宫内只能出现一次。

![figure.2](https://upload.wikimedia.org/wikipedia/commons/thumb/f/ff/Sudoku-by-L2G-20050714.svg/250px-Sudoku-by-L2G-20050714.svg.png)

上图是一个部分填充的有效的数独。

数独部分空格内已填入了数字，空白格用 '.' 表示。
```
示例 1:

输入:
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: true
示例 2:

输入:
[
  ["8","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
输出: false
解释: 除了第一行的第一个数字从 5 改为 8 以外，空格内其他数字均与 示例1 相同。
     但由于位于左上角的 3x3 宫内有两个 8 存在, 因此这个数独是无效的。
说明:

一个有效的数独（部分已被填充）不一定是可解的。
只需要根据以上规则，验证已经填入的数字是否有效即可。
给定数独序列只包含数字 1-9 和字符 '.' 。
给定数独永远是 9x9 形式的。
```

## 思维导图
![figure.1](https://gitee.com/zyp521/upload_image/raw/master/有效的数独.png)

## 代码
```
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        核心思想：
                实际就是一个大模拟
                分别进行如下判断如果有不满足的情况则结束判断，最坏时间复杂度情况就是判断全部情况
                1. 判断每行
                2. 判断每列
                3. 判断每个格子
                针对每行每列可以采用去掉所有"."然后set判断长度是否一致
        """
        nums = list(str(i) for i in range(1,10))
        # dictList = dict(zip(nums,[0 for i in range(10)]))
        # print(dictList)
        # 判断每行
        for i in range(9):
            dictList = dict(zip(nums,[0 for i in range(10)]))
            for j in range(9):
                if board[i][j] == '.':
                    continue
                dictList[board[i][j]] += 1
                if dictList[board[i][j]] >= 2:
                    return False

        # 判断每列
        for i in range(9):
            dictList = dict(zip(nums,[0 for i in range(10)]))
            for j in range(9):
                if board[j][i] == '.':
                    continue
                dictList[board[j][i]] += 1
                if dictList[board[j][i]] >= 2:
                    return False

        # 判断每个格子
        for i in range(9):
            dictList = dict(zip(nums, [0 for i in range(10)]))
            remainder = i % 3 # 余数
            consult = int(i / 3) # 商
            for j in range(3):
                for k in range(3):
                    if board[j+consult*3][k+remainder*3] == '.':
                        continue
                    dictList[board[j+consult*3][k+remainder*3]] += 1
                    if dictList[board[j+consult*3][k+remainder*3]] >= 2:
                        return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","5"]
]))
```