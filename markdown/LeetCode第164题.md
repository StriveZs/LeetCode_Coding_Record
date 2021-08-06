---
title: LeetCode No.164

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第164题—最大间距

各种排序我后面一定补上，大雾

自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个无序的数组，找出数组在排序之后，相邻元素之间最大的差值。

如果数组元素个数小于 2，则返回 0。
```
示例 1:

输入: [3,6,9,1]
输出: 3
解释: 排序后的数组是 [1,3,6,9], 其中相邻元素 (3,6) 和 (6,9) 之间都存在最大差值 3。
示例 2:

输入: [10]
输出: 0
解释: 数组元素个数小于 2，因此返回 0。
说明:

你可以假设数组中所有元素都是非负整数，且数值在 32 位有符号整数范围内。
请尝试在线性时间复杂度和空间复杂度的条件下解决此问题。
```
## 代码
```
#
# @lc app=leetcode.cn id=164 lang=python
#
# [164] 最大间距
#

# @lc code=start

class Solution(object):
    def time_out(self, nums):
        """
        题目要求在线性时间复杂度和空间复杂度上解决这个问题，因此最常用的排序之后在寻找最大间距大概率Time out不推荐，考虑其他方法
        [3 9 6 1] 线性复杂度的话，还是要考虑动态更新的问题，最好边排序边把最大间隔找出来，因此不仅要记录每个数字对应的最大间隔，还要找到全局最大的间隔
        那就考虑使用字典结构分别存储每个数值的最大间隔，然后每次更新最大间隔的话，
        最后更新全局最大间隔
        还有一点就是要找到线性时间排序的算法，即复杂度为o(n)
        根据网上的内容目前三种主要的线性时间排序算法分别为: 1.计数排序 2.基数排序 3.桶排序
        - 计数排序的思想: 对每一个输入元素x，确定小于x的个数，这样就可以把x直接放在它最终输出数组的位置上
        - 桶排序的思想: 将数组分到有限数量的桶子里，每个桶子在个别排序，当要被排序数组的数值是均匀分配的时候，桶排序可以是线性时间运行的
        - 基数排序的思想: 将所有待比较数值（正整数）统一为同样的数位长度，数位较短的数前面补零。然后，从最低位开始，依次进行一次排序。这样从最低位排序一直到最高位排序完成以后, 数列就变成一个有序序列。需要注意的是，对每一个数位进行排序的算法必须是稳定的，否则就会取消前一次排序的结果。通常我们使用计数排序或者桶排序作为基数排序的辅助算法
        
        这里我先使用插入排序来实现本问题，后续如果有时间的话，再学习一下上述三种线性时间排序
        插入排序裂开了，直接timeout
        :type nums: List[int]
        :rtype: int
        """
        # 特殊情况
        if len(nums) == 0 or len(nums) == 1:
            return 0
        
        # num_interval = dict()
        # 选择排序
        for i in range(0, len(nums)):
            # num_interval[nums[i]] = 0
            t = i
            for j in range(i+1, len(nums)):
                if nums[t] > nums[j]:
                    t = j
            temp = nums[t]
            nums[t] = nums[i]
            nums[i] = temp
            # # 更新所有数字的间隔
            # for m in range(0, i+1):
            #     if m == 0:
            #         num_interval[nums[m]] = abs(nums[1] - nums[0])
            #     elif m == len(nums)-1:
            #         num_interval[nums[m]] = abs(nums[m] - nums[m-1])
            #     else:
            #         num_interval[nums[m]] = max(abs(nums[m] - nums[m-1]), abs(nums[m] - nums[m+1]))
            max_interval = 0
        for i in range(len(nums)):
            if i == 0:
                max_interval = max(max_interval, abs(nums[1] - nums[0]))
            elif i ==len(nums)-1:
                max_interval = max(max_interval, abs(nums[i] - nums[i-1]))
            else:
                max_interval = max(max_interval, max(abs(nums[i] - nums[i-1]), abs(nums[i] - nums[i+1])))
        # return num_interval[max(num_interval,key=num_interval.get)]
        return max_interval
    def maximumGap(self, nums):
        """
        python中的sorted好像就是桶排序，这里偷懒直接用了，后面要去学习一下桶排序QAQ
        各种排序方法后面一定从头不上呜呜呜
        :type nums: List[int]
        :rtype: int
        """
        # 特殊情况
        if len(nums) == 0 or len(nums) == 1:
            return 0
        nums = sorted(nums)
        max_interval = 0
        for i in range(len(nums)):
            if i == 0:
                max_interval = max(max_interval, abs(nums[1] - nums[0]))
            elif i ==len(nums)-1:
                max_interval = max(max_interval, abs(nums[i] - nums[i-1]))
            else:
                max_interval = max(max_interval, max(abs(nums[i] - nums[i-1]), abs(nums[i] - nums[i+1])))
        return max_interval
# @lc code=end

s = Solution()
print(s.maximumGap([3,9,1,6]))
```