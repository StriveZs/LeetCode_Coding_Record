class Solution(object):
    # 动态规划——超时版本
    def timeout_canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        核心思想：
                类似之前做过的那道题《跳跃游戏II》，同样可以用动态规划来进行代码的编写
        """
        dp = [len(nums)+1 for i in range(len(nums))]  # 每个dp的值表示的是到当前位置的最小步数
        dp[0] = 0 # 表示到达第一个位置的最小步数为0

        for i in range(1,len(nums)): # 不算初始位置，选择从i之前位置到i的最短距离
            for j in range(0,i):
                if nums[j] >= i-j: # 表示可以一步从j到i
                    dp[i] = min(dp[i],dp[j]+1)

        if dp[-1] != len(nums)+1:
            return True
        else:
            return False

    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        核心思想:
                上个动态规划版本成功超时了，下面考虑用其他的办法
                其他的办法, 分为以下几点:
                    1) 从右往左考虑
                    2) 找到为0的位置，判断0之前是否有元素能够跨过0，如果没有则返回False
                    3) 除0之外的位置，由于不需要像跳跃游戏II中考虑最短步数，因此均可以到达
        """
        if 0 not in nums:
            return True
        if len(nums) == 1 and nums[0] == 0:
            return True
        i = len(nums)-2 # 从最后一个元素考虑
        while i >= 0:
            if nums[i] == 0:
                flag = True
                for j in range(0,i):
                    if nums[j] > i-j:
                        flag = False
                        break
                if flag:
                    return False
            i -= 1
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.canJump(nums = [3,2,1,0,4]))
