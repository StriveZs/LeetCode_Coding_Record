---
title: LeetCode No.16

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第十六题
## 题目描述

给定一个包括 n 个整数的数组 nums 和 一个目标值 target。找出 nums 中的三个整数，使得它们的和与 target 最接近。返回这三个数的和。假定每组输入只存在唯一答案。

 
```
示例：

输入：nums = [-1,2,1,-4], target = 1
输出：2
解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
 

提示：

3 <= nums.length <= 10^3
-10^3 <= nums[i] <= 10^3
-10^4 <= target <= 10^4
```

## 代码
```
class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        尝试使用双向指针的方式来进行查找, 要求事先结果进行排序
        """
        nums.sort()
        closeNum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(closeNum - target):
                    closeNum = s
                elif s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return target
        return closeNum

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))
```