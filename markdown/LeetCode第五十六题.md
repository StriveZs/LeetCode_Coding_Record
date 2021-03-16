---
title: LeetCode No.56

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第五十六题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间。

 
```
示例 1：
输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 

提示：

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
```

## 代码
```
class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]

        核心思想：
                依次判断:
                 1. 有交集且全包含的情况 A包含B和B包含A
                 2. 有交集且左包含的情况 [1,4] [0,1]  这个可以先对初始情况进行排序来解决
                 3. 有交集且右包含的情况 [0,2] [1,3]
                 3.如果两个区间没有交集，则放入result
        """
        intervals = sorted(intervals)
        result = []
        temp = intervals[0]
        i = 1
        while i < len(intervals):
            # 有交集且全包含的情况 A包含B
            if temp[0] >= intervals[i][0] and temp[1] <= intervals[i][1]:
                temp = intervals[i]
                i += 1
            # 有交集且全包含的情况 B包含A
            elif temp[0] <= intervals[i][0] and temp[1] >= intervals[i][1]:
                i += 1
            # 有交集且右包含
            elif temp[1] >= intervals[i][0]:
                tt = []
                tt.append(temp[0])
                tt.append(intervals[i][1])
                temp = tt
                i += 1
            else: # 下一个
                result.append(temp)
                temp = intervals[i]
                i += 1
        result.append(temp)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.merge(intervals = [[1,4],[0,1]]))
```