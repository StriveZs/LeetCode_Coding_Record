---
title: LeetCode No.40

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第四十题
## 题目描述
```
给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
```

## 代码
同样是回溯法，只是额外添加了需要确认是否重复使用该数。  

```
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        核心思想：
                分析题目同样可以看出我们应该使用回溯法进行求解
                去重的关键在于，若当前循环中的i等l则跳过
        回溯法的标准框架
        def backtrack(path, selected):
            if 满足停止条件：
                res.append(path)
            for 选择 in 选择列表：
                做出选择
                递归执行backtrack
                    满足则return True
                如果不满足要求就撤销选择
        """
        candidates.sort()
        result = []
        temp = candidates[0] - 1

        def backtrack(target, candidates, temp, result, path, start):
            for i in range(start, len(candidates)):
                if candidates[i] == temp:
                    continue
                path.append(candidates[i])
                if sum(path) < target:
                    backtrack(target, candidates, temp, result, path, i + 1)
                elif sum(path) == target:
                    result.append(path[:])
                    path.pop()
                    return
                else:
                    path.pop()
                    return
                temp = path.pop()
        backtrack(target, candidates, temp, result, [], 0)
        # print(result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))

```