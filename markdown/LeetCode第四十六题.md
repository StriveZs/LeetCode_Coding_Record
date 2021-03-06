---
title: LeetCode No.46

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第四十六题
刚开学，果壳开学挺晚的，这几天忙着收拾，今天才有空接着更新！！！

科研生活开始咯。  

## 题目描述
给定一个 没有重复 数字的序列，返回其所有可能的全排列。

示例:
```
输入: [1,2,3]
输出:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]
```

## 代码
经典回溯法。  

```
class Solution(object):
    def permute(self, nums):
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
                if nums in result:
                    return False
                else:
                    result.append(temp[:])
                    return True
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
    print(s.permute([1,2,3]))
```