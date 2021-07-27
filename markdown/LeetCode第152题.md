---
title: LeetCode No.152

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第152题—乘积最大子数组

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你一个整数数组 nums ，请你找出数组中乘积最大的连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

 
```
示例 1:

输入: [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
```
## 代码
```
class Solution(object):
    def maxProduct(self, nums):
        """
        考虑使用动态规划. 因为数组中的值包含了正值和负值，可能会变为负负得正，或者你最大的正值乘个-1就会变为最小的负值
        因此考虑使用两个数组来进行记录，分别记录当前的最大值和最小值, 然后进行后续应用
        :type nums: List[int]
        :rtype: int
        """
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        dp = [0] * len(nums)
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            dp[i] = max(max_dp[i], dp[i-1])
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-1, -2, -9, 6]))

```