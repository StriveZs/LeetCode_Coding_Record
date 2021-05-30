import sys
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        利用动态规划
        """
        if len(prices) == 1:
            return 0
        # 五种状态初始化
        dp0 = 0
        dp1 = -prices[0]
        dp2 = -sys.maxsize
        dp3 = -sys.maxsize
        dp4 = -sys.maxsize
        # 状态转移
        for i in range(1,len(prices)):
            dp1 = max(dp1, dp0-prices[i]) # 可能是从dp0买入一笔转移过来的，但是没有卖出因此为-prices[i]，也可能是一直处于dp1没有卖出
            dp2 = max(dp2, dp1+prices[i]) # 可能是从dp1卖出一笔转移过来的，因为卖出了所以为+prices[i],也可能是因为没有买一直停留在dp2
            dp3 = max(dp3, dp2-prices[i])
            dp4 = max(dp4, dp3+prices[i])
        return dp4 #返回最终状态，就是最终的利润
    
if __name__ == '__main__':
    s  = Solution()
    print(s.maxProfit([3,3,5,0,0,3,1,4]))