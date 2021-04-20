---
title: LeetCode No.88

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第八十七题—扰乱字符串
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给你两个有序整数数组 nums1 和 nums2，请你将 nums2 合并到 nums1 中，使 nums1 成为一个有序数组。

初始化 nums1 和 nums2 的元素数量分别为 m 和 n 。你可以假设 nums1 的空间大小等于 m + n，这样它就有足够的空间保存来自 nums2 的元素。

```

示例 1：

输入：nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
输出：[1,2,2,3,5,6]
示例 2：

输入：nums1 = [1], m = 1, nums2 = [], n = 0
输出：[1]
 

提示：

nums1.length == m + n
nums2.length == n
0 <= m, n <= 200
1 <= m + n <= 200
-109 <= nums1[i], nums2[i] <= 109
```

## 代码
```
class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.

        核心思想：
                前提两个序列是按照从小到大排序好的
                对nums2进行倒序和nums1的数值进行倒序比较
                如果nums2[i]的数值大于nums1最大的值 则nums1[end]=nums[i]
                如果nums2[i]的数值小于nums1最大值，则先将nums1最大值排在序列末尾非0位置
                如果nums2[i]的数值小于num1某个值，则将nums1该值后移到序列末尾非0位置(非0位置可以用下标记录)

                实质上：就是比较nums1和nums2谁大，谁就置到末尾
        """
        if n == 0:
            return nums1
        if m == 0:
            nums1[:]=nums2[:]
            return nums1
        index = m + n - 1  # 记录末尾位置下标
        m,n = m - 1,n - 1 # nums1和nums2正确下标
        while m >= 0 and n >= 0:
            if nums1[m] > nums2[n]:
                nums1[index] = nums1[m]
                m = m - 1
            else:
                nums1[index] = nums2[n]
                n = n - 1
            index = index-1
        # 处理nums1被处理完nums2没被处理完的情况
        while n >= 0:
            nums1[index] = nums2[n]
            index,n = index-1,n-1
        return nums1

if __name__ == '__main__':
    s = Solution()
    print(s.merge(nums1 = [2,0], m = 1, nums2 = [1], n = 1))
```