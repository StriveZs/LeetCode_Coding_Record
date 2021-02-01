class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        result = []
        for i in range(len(nums)):
            if nums[i] != val:
                result.append(nums[i])
        nums[0:len(result)] = result
        return len(result)

if __name__ == '__main__':
    s = Solution()
    print(s.removeElement(nums = [3,2,2,3], val = 3))