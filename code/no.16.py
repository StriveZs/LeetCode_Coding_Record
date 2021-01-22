class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        尝试使用双向指针的方式来进行查找, 要求事先结果进行排序
        """
        nums.sort()
        closeNum = nums[0] + nums[1] + nums[2]
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if abs(s - target) < abs(closeNum - target):
                    closeNum = s
                elif s > target:
                    r -= 1
                elif s < target:
                    l += 1
                else:
                    return target
        return closeNum

if __name__ == '__main__':
    s = Solution()
    print(s.threeSumClosest([-1,2,1,-4], 1))