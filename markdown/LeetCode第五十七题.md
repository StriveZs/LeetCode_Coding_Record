---
title: LeetCode No.57

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第五十七题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)
## 题目描述
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 
```
示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
示例 3：

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]
示例 4：

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]
示例 5：

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]
 

提示：

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals 根据 intervals[i][0] 按 升序 排列
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105
```

## 代码
```
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        
        核心思想：
                就是no.56的变形，只需要在开头把需要插入的区间添加到列表中
                然后在进行56题的操作即可
                依次判断:
                 1. 有交集且全包含的情况 A包含B和B包含A
                 2. 有交集且左包含的情况 [1,4] [0,1]  这个可以先对初始情况进行排序来解决
                 3. 有交集且右包含的情况 [0,2] [1,3]
                 3.如果两个区间没有交集，则放入result
        """
        intervals.append(newInterval)
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
            else:  # 下一个
                result.append(temp)
                temp = intervals[i]
                i += 1
        result.append(temp)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))
```