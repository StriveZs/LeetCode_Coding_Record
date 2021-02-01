class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        temp = set(nums)
        result = sorted(list(temp))
        nums[0:len(result)] = result  # 注意为了能够AC需要将nums前x个替换为去重之后的数组
        return len(result)

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates(nums = [1,1,2]))