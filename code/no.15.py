class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        尝试使用双向指针的方式来进行查找，这样可以去除一个循环，关键点是进行边界的收缩
        """
        nums.sort()
        result = []
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s == 0:
                    temp = [nums[i], nums[l], nums[r]]
                    # 去重
                    if temp in result:
                        pass
                    else:
                        result.append(temp)
                    l += 1
                    r -= 1
                    # 剪枝操作 目的是收缩边界
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1
                    while r > l and nums[r] == nums[r + 1]:
                        r -= 1
                elif s > 0:
                    r -= 1
                else:
                    l += 1
        return result



    def Version_timeout(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums = sorted(nums)
        resultult = []
        if len(nums) <=2:
            return resultult
        for i in range(len(nums)):
            temp = []
            j = i+1
            while j < len(nums):
                k = j+1
                while k < len(nums):
                    if nums[i] + nums[j] + nums[k] == 0:
                        temp.append(nums[i])
                        temp.append(nums[j])
                        temp.append(nums[k])
                        if sorted(temp) in resultult:
                            pass
                        else:
                            resultult.append(sorted(temp))
                        temp = []
                    k += 1
                j += 1
        
        return resultult

if __name__ == '__main__':
    s = Solution()
    print(s.threeSum([-1,0,1,2,-1,-4]))