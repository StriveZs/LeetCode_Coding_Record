class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int

        核心思想:
            采用动态规划的方法
            时间复杂度为O(n)
            记录在i之前的最大利润，并和当前利润比较
            记录i天之前的最小值
        """
        if len(prices) == 1:
            return 0
        dp = [0] * len(prices)
        min_value = prices[0]
        max_value = 0
        for i in range(1,len(prices)):
            max_value = max(max_value, prices[i] - min_value) # 记录最大利润
            min_value = min(min_value,prices[i]) # 记录第i天之前的最小值
        return max_value

if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([7,6,4,3,1]))