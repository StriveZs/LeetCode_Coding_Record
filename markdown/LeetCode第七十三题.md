---
title: LeetCode No.73

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第七十三题—矩阵置零
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个 m x n 的矩阵，如果一个元素为 0 ，则将其所在行和列的所有元素都设为 0 。请使用 原地 算法。

进阶：

一个直观的解决方案是使用  O(mn) 的额外空间，但这并不是一个好的解决方案。
一个简单的改进方案是使用 O(m + n) 的额外空间，但这仍然不是最好的解决方案。
你能想出一个仅使用常量空间的解决方案吗？

![figure.1](https://assets.leetcode.com/uploads/2020/08/17/mat1.jpg)
```

示例 1：


输入：matrix = [[1,1,1],[1,0,1],[1,1,1]]
输出：[[1,0,1],[0,0,0],[1,0,1]]
```
![figure.2](https://assets.leetcode.com/uploads/2020/08/17/mat2.jpg)
```
示例 2：


输入：matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
输出：[[0,0,0,0],[0,4,5,0],[0,3,1,0]]
 

提示：

m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
```

## 代码
```
import numpy as np

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        核心思想：
                观察例子可以看出被变成0的值不会被判断为需要将其所在的行和列置为0
                可以考虑使用一个和输入矩阵对应大小的标志矩阵(用来表示当前访问的位置是本来0还是被变成0的 要进行区分，才能避免出现上述情况)
                然后就是依次遍历矩阵，当一个值等于0的之后，则把它所在行和列的值均变为0，并且修改对应的标志矩阵
        """
        row = len(matrix) # 行数
        colum = len(matrix[0]) # 列数
        flagMatrix = np.ones(shape=(row,colum),dtype=bool) # 标志矩阵
        # print(flagMatrix)
        for i in range(row):
            for j in range(colum):
                if flagMatrix[i][j] and matrix[i][j] == 0:
                    # 将所在行的所有元素均设为0
                    for k in range(colum):
                        # 去除本来就为0的情况
                        if matrix[i][k] == 0:
                            continue
                        matrix[i][k] = 0
                        flagMatrix[i][k] = False
                    # 将所在列的所有元素均设为0
                    for k in range(row):
                        # 去除本来就为0的情况
                        if matrix[k][j] == 0:
                            continue
                        matrix[k][j] = 0
                        flagMatrix[k][j] = False
        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))
```