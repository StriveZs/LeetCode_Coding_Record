class Solution(object):
    def maxProduct(self, nums):
        """
        考虑使用动态规划. 因为数组中的值包含了正值和负值，可能会变为负负得正，或者你最大的正值乘个-1就会变为最小的负值
        因此考虑使用两个数组来进行记录，分别记录当前的最大值和最小值, 然后进行后续应用
        :type nums: List[int]
        :rtype: int
        """
        max_dp = [0] * len(nums)
        min_dp = [0] * len(nums)
        dp = [0] * len(nums)
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            max_dp[i] = max(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            min_dp[i] = min(max_dp[i-1] * nums[i], min_dp[i-1] * nums[i], nums[i])
            dp[i] = max(max_dp[i], dp[i-1])
        return dp[-1]

if __name__ == '__main__':
    s = Solution()
    print(s.maxProduct([-1, -2, -9, 6]))
