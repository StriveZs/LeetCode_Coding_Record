class Solution(object):
    def findMin(self, nums):
        """
        分析：
            感觉题目的意思可以看出本题的实质是找到分断点(因为原数组是有序数组)
            因此从两端开始判断的话，只需找到比较小的那一端，然后从小的那一端开始判断
            1.如果是从左端开始的话，如果nums[i] <= nums[i+1]，则继续右移，直到不满足结果
            2. 如果是从右端开始的话，如果nums[i] <= nums[i+1], 则继续左移，直到不满足结果
        :type nums: List[int]
        :rtype: int
        """
        flag = True
        if nums[0] < nums[-1]:
            flag = True # 从左端开始找
        else:
            flag = False # 从右端开始找

        for i in range(1, len(nums)):
            if flag:
                if nums[i] < nums[i-1]:
                    return nums[i]
            else:
                if nums[len(nums) - i] < nums[len(nums) - 1 - i]:
                    return nums[len(nums) - i]
        return nums[0]
if __name__ == '__main__':
    s = Solution()
    print(s.findMin(nums = [1,2,3,4,5]))
