---
title: LeetCode No.90

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第九十题—子集II
## 题目描述
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

```
示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
```

## 代码
```
class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        核心思想：
                经典回溯法
                def backtrack(path, selected):
                    if 满足停止条件：
                        res.append(path)
                    for 选择 in 选择列表：
                        做出选择
                        递归执行backtrack
                            满足则return True
                        如果不满足要求就撤销选择
        魔改78题就可以了
        只需要对生成的结果进行排序，然后判断是否在集合中，如果出现则不行
        """
        res = []
        res.append([])
        numsLen = len(nums)
        temp = []

        def backtrack(temp, l, numsLen, length):
            # 停止条件
            if len(temp) == length:
                t_1 = sorted(temp)
                if t_1 not in res:
                    tt = copy.copy(t_1)
                    res.append(tt)
                    return

            for j in range(l + 1, numsLen):
                # 做出选择
                temp.append(nums[j])
                # 递归执行
                backtrack(temp, j, numsLen, length)
                # 撤销选择
                temp.pop()

        # 递归调用  length值不同
        for i in range(1, numsLen + 1):
            backtrack(temp, -1, numsLen, i)
        return res
```