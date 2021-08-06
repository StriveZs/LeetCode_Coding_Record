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

