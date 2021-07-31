---
title: LeetCode No.154

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第154题—寻找旋转排序数组中的最小值 II

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,4,4,5,6,7] 在变化后可能得到：
- 若旋转 4 次，则可以得到 [4,5,6,7,0,1,4]
- 若旋转 7 次，则可以得到 [0,1,4,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个可能存在 重复 元素值的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

```

示例 1：

输入：nums = [1,3,5]
输出：1
示例 2：

输入：nums = [2,2,2,0,1]
输出：0
 

提示：

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
```
## 代码
```
class Solution(object):
    def findMin(self, nums):
        """
        除了return min(nums)之外的考虑，延续上一道题的想法
        :type nums: List[int]
        :rtype: int
        """
        flag = True
        if nums[0] < nums[-1]:
            flag = True  # 从左端开始找
        else:
            flag = False  # 从右端开始找

        for i in range(1, len(nums)):
            if flag:
                if nums[i] < nums[i - 1]:
                    return nums[i]
            else:
                if nums[len(nums) - i] < nums[len(nums) - 1 - i]:
                    return nums[len(nums) - i]
        return nums[0]

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2,2,2,0,1]))
```