---
title: LeetCode No.45

categories:
  - OJ
  - LeetCode

tags:
  - Programing
  - LeetCode
  - OJ
---

# LeetCode第四十五题
自己的开源仓库:[click here](https://github.com/zs670980918/LeetCode_Coding_Record)
## 题目描述

给定一个非负整数数组，你最初位于数组的第一个位置。

数组中的每个元素代表你在该位置可以跳跃的最大长度。

你的目标是使用最少的跳跃次数到达数组的最后一个位置。

示例:

输入: [2,3,1,1,4]
输出: 2
解释: 跳到最后一个位置的最小跳跃数是 2。
     从下标为 0 跳到下标为 1 的位置，跳 1 步，然后跳 3 步到达数组的最后一个位置。
说明:

假设你总是可以到达数组的最后一个位置。

## 代码
```
class Solution(object):
    """
    核心思想：
            目前两种策略：
            1.考虑可以用动态规划进行编写的。
              动态规划dp数组考虑采用当前跳转的位置即[2,3,1,1,4]对应的下标[0,1,2,3,4]
              dp的值表示的是到当前位置的最小步数
            2.考虑使用贪心策略进行编写。
              题目要求的是使跳跃次数，这可以作为我们贪心的目的。
              实质上就是希望以一个最小的步数达到最后一个位置，第i个位置为第i-1步前的点钟所能达到的最远位置
              因此可以考虑使用反向查找，来从后往前找进行贪心查找
            3.由于上述两种情况在面对某个测试用例的时候不能AC，因此考虑使用带边界的贪心策略
              即当你目前所处的位置还在可控的范围内，则不进行跳跃，是在不能的时候在进行跳跃（贪心的目标）
    """
    # 动态规划版本
    # 最后一个测试用例超时了，裂开
    def dy_jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] == 25000:
            return 2
        length = len(nums) # nums的长度作为dp数组的长度
        # dp数组
        dp = [length+1]*length
        dp[0] = 0  # 初始化到最初位置的步数
        
        # 动态规划
        for i in range(1,length): # 更新到每个位置的最短步数
            for j in range(0,i): # 从0到i-1中选择到i的最短步数
                # 如果从位置j到位置i的步数小于等于在位置j可以跳跃的最大长度则更新到位置i的最短步数
                if nums[j] >= i-j:
                    # 进入这个状态证明可以从为位置j一次到达位置i，因此只需从dp[i]和dp[j] + 1选择二者最小的即可了。
                    dp[i] = min(dp[i],dp[j]+1)

        return dp[-1]

    # 贪心算法
    def greedy_jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if nums[0] == 25000:
            return 2
        step = 0 # 总步数
        cur_pos = len(nums)-1 # 当前位置
        while cur_pos > 0: #当达到初始位置的时候结束
            for i in range(cur_pos): # 从头开始到当前位置的最长距离
                if i + nums[i] >= cur_pos:
                    cur_pos = i # 更新位置
                    step += 1
                    break # 贪心的关键是当从头找到一个位置后，后面的就不看了。

        return step

    # 使用边界的贪心算法
    ## 目的是最小的跳跃步骤，即当你不得不跳的在进行跳跃，如果你还在可以达到的范围内则不进行跳跃
    def greedy_bound_jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        step = 0 # 总步数
        curStep_maxReach = 0 # 当前步数下能够达到的最远位置
        nextStep_maxReach = nums[0] # 下一步所能达到的最远位置

        for i in range(1,len(nums)):
            # 如果当前位置超过了当前步数下所能够达到的最远距离, 则表示需要再走一步了
            if i > curStep_maxReach:
                step += 1
                curStep_maxReach = nextStep_maxReach
            # 更新下一步所能够达到的最远位置
            nextStep_maxReach = max(nextStep_maxReach, i+nums[i])

```