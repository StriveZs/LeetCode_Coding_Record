---
title: LeetCode No.121

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---


# LeetCode第121题—买卖股票的最佳时机
自己代码的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)  欢迎Star和Fork :)

## 题目描述
给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。

你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。设计一个算法来计算你所能获取的最大利润。

返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

```

示例 1：

输入：[7,1,5,3,6,4]
输出：5
解释：在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
     注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格；同时，你不能在买入前卖出股票。
示例 2：

输入：prices = [7,6,4,3,1]
输出：0
解释：在这种情况下, 没有交易完成, 所以最大利润为 0。
 
提示：

1 <= prices.length <= 105
0 <= prices[i] <= 104
```
## 代码
```
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
```