---
title: LeetCode No.85

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第八十五题—最大矩形
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
我是笨比我是笨比，这都没想到，只能看大佬的解法，在自己写。我太菜了！！！

给定一个仅包含 0 和 1 、大小为 rows x cols 的二维二进制矩阵，找出只包含 1 的最大矩形，并返回其面积。

![figure.1](https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg)
 
```
示例 1：

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
示例 2：

输入：matrix = []
输出：0
示例 3：

输入：matrix = [["0"]]
输出：0
示例 4：

输入：matrix = [["1"]]
输出：1
示例 5：

输入：matrix = [["0","0"]]
输出：0
 

提示：

rows == matrix.length
cols == matrix[0].length
0 <= row, cols <= 200
matrix[i][j] 为 '0' 或 '1'
```

## 解法
类似84题，这里将矩阵对每行进行统计，分别得到每行对应的高度，这样就可以求得最大矩阵，具体参考图例十分清楚.

![figure.2](https://gitee.com/zyp521/upload_image/raw/master/DU5Jfz.png)

希望能根据这道题的解法，以后举一反三。

## 代码
```
class Solution(object):
    def monotonicStack(self, heights):
        """
        :argument  利用no.84题的解法
        """
        # 处理height 前后分别添加0 方便单调栈处理
        heights.insert(0, 0)
        heights.append(0)
        stack = [] # 单调增栈
        maxLineArea = 0 # 最大行面积（这一行对应的面积）
        for i in range(len(heights)):
            while len(stack) != 0 and heights[stack[len(stack)-1]] > heights[i]:
                current = stack[len(stack)-1]
                stack.pop()  # 出栈
                left = stack[len(stack)-1]+1 # 获得左边界
                right = i-1 # 获得右边界
                maxLineArea = max(maxLineArea,(right-left+1)*heights[current])
            stack.append(i)
        return maxLineArea

    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int

        核心思想：
                考虑使用单调栈来编写
                先将输入拆分成一些列的柱状图（每行拆一次），我们只需要计算每个柱状图中的最大面积，并找到全局最大值
        """

        maxArea = 0 # 最大面积记录  面积要求是矩形才能计算
        # 一行一行的访问
        for i in range(len(matrix)):
            heights = [] # 当前行对应的柱状图高度存储
            for j in range(len(matrix[0])):
                # 统计每一列对应的高度
                num = 0 # 高度记录
                for t in range(0,i+1):
                    if matrix[i-t][j] == '1':
                        num += 1
                    else:
                        break
                heights.append(num)
            maxArea = max(maxArea,self.monotonicStack(heights)) # 调用单调栈处理
        return maxArea

if __name__ == '__main__':
    s = Solution()
    print(s.maximalRectangle(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]))
```