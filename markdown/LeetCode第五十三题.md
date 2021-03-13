---
title: LeetCode No.53

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第五十三题
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Folk :)
## 题目描述
给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

 
```
示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [0]
输出：0
示例 4：

输入：nums = [-1]
输出：-1
示例 5：

输入：nums = [-100000]
输出：-100000
 

提示：

1 <= nums.length <= 3 * 104
-105 <= nums[i] <= 105
```

## 代码
```
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        核心思想: 1. 暴力法：遍历所有情况吧，采用适当的剪枝
                2. 动态规划：突然想到可以采用动态规划的方法
        """
        # 本题就采用动态规划的方法
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            result = max(result,dp[i])
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray(nums = [1]))
```