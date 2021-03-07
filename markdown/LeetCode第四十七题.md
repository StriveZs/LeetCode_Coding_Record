---
title: LeetCode No.47

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第四十七题

## 题目描述
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：
```
输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10
```

## 代码
本题和上一道题目异曲同工，只是添加一个额外的重复检测代码。

```
class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        核心思想：这里Python有现成的库可以进行，但是为了能够掌握代码，这里我使用回溯法进行编写代码

        回溯法的框架：
            def backtrack(path, selected):
                if 满足停止条件：
                    res.append(path)
                for 选择 in 选择列表：
                    做出选择
                    递归执行backtrack
                        满足则return True
                    如果不满足要求就撤销选择
        """
        result = []
        temp = []
        def backtrack(nums):
            if not nums: # 如果为空则表示选择完毕
                if temp in result:
                    return
                else:
                    result.append(temp[:])
                    return
            for i in range(len(nums)):
                # 做出选择
                temp.append(nums[i])
                # 去除做出的选择
                tt = nums[:i]+nums[i+1:]
                # 接着执行选择
                backtrack(tt)
                # 撤销选择
                temp.pop()
        backtrack(nums)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,2,3]))
```