#
# @lc app=leetcode.cn id=169 lang=python3
#
# [169] 多元数组
#

# @lc code=start
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

# s = Solution()
# print(s.majorityElement())

# @lc code=end

