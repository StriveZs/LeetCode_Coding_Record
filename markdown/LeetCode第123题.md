---
title: LeetCode No.123

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第123题—买卖股票的最佳时机III
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。

设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。

注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

```

示例 1:

输入：prices = [3,3,5,0,0,3,1,4]
输出：6
解释：在第 4 天（股票价格 = 0）的时候买入，在第 6 天（股票价格 = 3）的时候卖出，这笔交易所能获得利润 = 3-0 = 3 。
     随后，在第 7 天（股票价格 = 1）的时候买入，在第 8 天 （股票价格 = 4）的时候卖出，这笔交易所能获得利润 = 4-1 = 3 。
示例 2：

输入：prices = [1,2,3,4,5]
输出：4
解释：在第 1 天（股票价格 = 1）的时候买入，在第 5 天 （股票价格 = 5）的时候卖出, 这笔交易所能获得利润 = 5-1 = 4 。   
     注意你不能在第 1 天和第 2 天接连购买股票，之后再将它们卖出。   
     因为这样属于同时参与了多笔交易，你必须在再次购买前出售掉之前的股票。
示例 3：

输入：prices = [7,6,4,3,1] 
输出：0 
解释：在这个情况下, 没有交易完成, 所以最大利润为 0。
示例 4：

输入：prices = [1]
输出：0
 

提示：

1 <= prices.length <= 105
0 <= prices[i] <= 105
```
## 题解
参考大佬的动态规划思想做出来的。我是菜逼我是菜逼

![figure.1](https://gitee.com/zyp521/upload_image/raw/master/IMG_0712.PNG)

## 代码
```
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
```