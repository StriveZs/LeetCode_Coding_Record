class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        核心思想: 1. 暴力法：遍历所有情况吧，采用适当的剪枝
                2. 动态规划：突然想到可以采用动态规划的方法
        """
        # 本题就采用动态规划的方法
        dp = [0 for i in range(len(nums))]
        dp[0] = nums[0]
        result = dp[0]
        for i in range(1,len(nums)):
            dp[i] = max(dp[i-1]+nums[i],nums[i])
            result = max(result,dp[i])
        return result
    
if __name__ == '__main__':
    s = Solution()
    print(s.maxSubArray(nums = [1]))