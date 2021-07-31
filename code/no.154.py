class Solution(object):
    def findMin(self, nums):
        """
        除了return min(nums)之外的考虑，延续上一道题的想法
        :type nums: List[int]
        :rtype: int
        """
        flag = True
        if nums[0] < nums[-1]:
            flag = True  # 从左端开始找
        else:
            flag = False  # 从右端开始找

        for i in range(1, len(nums)):
            if flag:
                if nums[i] < nums[i - 1]:
                    return nums[i]
            else:
                if nums[len(nums) - i] < nums[len(nums) - 1 - i]:
                    return nums[len(nums) - i]
        return nums[0]

if __name__ == '__main__':
    s = Solution()
    print(s.findMin([2,2,2,0,1]))