---
title: LeetCode No.81

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第八十一题—搜索旋转排序数组II
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

```

示例 1：

输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
示例 2：

输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
 

提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104
```

## 代码
执行用时：40 ms, 在所有 Python3 提交中击败了71.73%的用户内存消耗：15.2 MB, 在所有 Python3 提交中击败了63.12%的用户

代码写的太垃圾了:

```
class Solution(object):
    # 二分搜索
    def binarySearch(self,nums,start,ends,target):
        if ends < start:
            return False
        mid = int((start+ends)/2)
        if nums[mid] == target:
            return True
        else:
            if nums[mid] > target:
                return self.binarySearch(nums,start,mid-1,target)
            elif nums[mid] < target:
                return self.binarySearch(nums,mid+1,ends,target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool

        核心思想：
                考虑：寻找划分点，在这期间如果匹配到target则不用在查找了直接返回True
                    如果没找到，则直接将划分点之后的数组进行二分查找即可。
        """
        if len(nums) == 1:
            if nums[0] != target:
                return False
            else:
                return True
        # 寻找旋转点
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == target:
                    return True
            if nums[i] == target: # 直接匹配到情况
                return True
            elif nums[i] < nums[i-1]:
                return self.binarySearch(nums[i:],0,len(nums[i:])-1,target)
        return self.binarySearch(nums,0,len(nums)-1,target) # 单独处理全是相同数字的情况

if __name__ == '__main__':
    s = Solution()
    #print(s.binarySearch([1,2,3,4],0,3,1))
    print(s.search(nums = [3,1], target = 0))

```