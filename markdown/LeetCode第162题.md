# LeetCode第162题
---
title: LeetCode No.162

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第162题—寻找峰值

前几天老忘了更新，我错了。QAQ  
最新研究一下VSCode刷LeetCode好方便好舒服。

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
峰值元素是指其值大于左右相邻值的元素。

给你一个输入数组 nums，找到峰值元素并返回其索引。数组可能包含多个峰值，在这种情况下，返回 任何一个峰值 所在位置即可。

你可以假设 nums[-1] = nums[n] = -∞ 。

``` 

示例 1：

输入：nums = [1,2,3,1]
输出：2
解释：3 是峰值元素，你的函数应该返回其索引 2。
示例 2：

输入：nums = [1,2,1,3,5,6,4]
输出：1 或 5 
解释：你的函数可以返回索引 1，其峰值元素为 2；
     或者返回索引 5， 其峰值元素为 6。
 

提示：

1 <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
对于所有有效的 i 都有 nums[i] != nums[i + 1]
```
## 代码
```
#
# @lc app=leetcode.cn id=162 lang=python
#
# [162] 寻找峰值
#

# @lc code=start
class Solution(object):
    def findPeakElement(self, nums):
        """
        峰值元素是指其值大于左右相邻值的元素，nums[-1] = nums[n] = -∞ 
        那么就表示只要第一个元素大于它右边的元素，就是峰值，最后一个元素大于它左边的元素，就是峰值
        其他的遍历就好了
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return None
        if len(nums) == 1:
            return 0
        res = [] # 结果存储
        for i in range(len(nums)):
            if i == 0:
                if nums[i] > nums[i+1]:
                    return i
                    
            elif i == len(nums)-1:
                if nums[i] > nums[i-1]:
                    return i
            else:
                if nums[i] > nums[i-1] and nums[i] > nums[i+1]:
                    return i
        return None
# @lc code=end


```