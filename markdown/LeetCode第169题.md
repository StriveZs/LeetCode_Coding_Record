---
title: LeetCode No.169

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第169题
## 题目描述
给定一个大小为 n 的数组 nums ，返回其中的多数元素。多数元素是指在数组中出现次数 大于 ⌊ n/2 ⌋ 的元素。

你可以假设数组是非空的，并且给定的数组总是存在多数元素。

 

示例 1：

输入：nums = [3,2,3]
输出：3
示例 2：

输入：nums = [2,2,1,1,1,2,2]
输出：2
 

提示：
n == nums.length
1 <= n <= 5 * 104
-109 <= nums[i] <= 109
 

进阶：尝试设计时间复杂度为 O(n)、空间复杂度为 O(1) 的算法解决此问题。

## 代码
```
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n = len(nums)
        dists = dict()
        res = []
        for i in range(n):
            if nums[i] not in dists.keys():
                dists[nums[i]] = 1
            else:
                dists[nums[i]] += 1
            
        for key in dists.keys():
            if dists[key] > (n / 2):
                return key
```

取巧方法，因为多数元素必然存在，那么对数组进行排序(sort)之后，从往前找就可以了。