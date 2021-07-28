---
title: LeetCode No.153

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第153题—寻找旋转排序数组中的最小值

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

 
```
示例 1：

输入：nums = [3,4,5,1,2]
输出：1
解释：原数组为 [1,2,3,4,5] ，旋转 3 次得到输入数组。
示例 2：

输入：nums = [4,5,6,7,0,1,2]
输出：0
解释：原数组为 [0,1,2,4,5,6,7] ，旋转 4 次得到输入数组。
示例 3：

输入：nums = [11,13,15,17]
输出：11
解释：原数组为 [11,13,15,17] ，旋转 4 次得到输入数组。
 

提示：

n == nums.length
1 <= n <= 5000
-5000 <= nums[i] <= 5000
nums 中的所有整数 互不相同
nums 原来是一个升序排序的数组，并进行了 1 至 n 次旋转
```
## 代码
### 非常不推荐
没意义.
```
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return min(nums)
```
### 正确思路
```
class Solution(object):
    def findMin(self, nums):
        """
        分析：
            感觉题目的意思可以看出本题的实质是找到分断点(因为原数组是有序数组)
            因此从两端开始判断的话，只需找到比较小的那一端，然后从小的那一端开始判断
            1.如果是从左端开始的话，如果nums[i] <= nums[i+1]，则继续右移，直到不满足结果
            2. 如果是从右端开始的话，如果nums[i] <= nums[i+1], 则继续左移，直到不满足结果
        :type nums: List[int]
        :rtype: int
        """
        flag = True
        if nums[0] < nums[-1]:
            flag = True # 从左端开始找
        else:
            flag = False # 从右端开始找

        for i in range(1, len(nums)):
            if flag:
                if nums[i] < nums[i-1]:
                    return nums[i]
            else:
                if nums[len(nums) - i] < nums[len(nums) - 1 - i]:
                    return nums[len(nums) - i]
        return nums[0]
if __name__ == '__main__':
    s = Solution()
    print(s.findMin(nums = [1,2,3,4,5]))

```