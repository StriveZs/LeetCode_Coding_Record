---
title: LeetCode No.74

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第七十四题—搜索二维矩阵
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。

![figure.1](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)

```
示例 1：

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
```

![figure.2](https://gitee.com/zyp521/upload_image/raw/master/jfxZce.jpg)

```
示例 2：

输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104
```
## 代码
```
class Solution(object):
    # 二分法
    def binarySearch(self, source, target, head, end):
        if head > end:
            return False
        mid = int((head + end)/2)
        if target == source[mid]:
            return True
        elif target > source[mid]:
            return self.binarySearch(source,target,mid+1,end)
        elif target < source[mid]:
            return self.binarySearch(source,target,head,mid-1)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        核心思想:
                可以先搜索目标数据可能在哪行，通过跟行首进行对比可得
                然后使用二分法进行搜索该行所有的元素，如果满足则返回true，否则返回false
        """
        for i in range(len(matrix)):
            if i == len(matrix)-1:
                return self.binarySearch(matrix[i],target,0,len(matrix[i])-1)
            else:
                if target >= matrix[i][0] and target < matrix[i+1][0]:
                    return self.binarySearch(matrix[i], target, 0, len(matrix[i])-1)
        return False

if __name__ == '__main__':
    s = Solution()
    # print(s.binarySearch([1,2,3,4,5],6,0,5-1))
    print(s.searchMatrix(matrix = [[1]], target = 3))
```