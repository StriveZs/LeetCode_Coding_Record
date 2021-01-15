class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        result_index = []
        flag = False
        length = len(nums)
        for i in range(length):
            j = i+1
            while j < length:
                if nums[i] + nums[j] == target:
                    flag = True
                    result_index.append(i)
                    result_index.append(j)
                    break
                j = j + 1
            if flag:
                break
        return result_index

if __name__ == '__main__':
    nums = [3,2,4]
    target = 6
    s = Solution()
    print(s.twoSum(nums,target))
