class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        length = len(nums) # 总长度
        index_a = length - 1
        # 从后往前找
        while index_a >= 0:
            index_b = length - 1
            while index_b > index_a :
                # 如果大于则交换位置并对前面查找的内容进行排序
                if nums[index_b] > nums[index_a]:
                    temp = nums[index_a]
                    nums[index_a] = nums[index_b]
                    nums[index_b] = temp
                    tt = nums[index_a + 1:len(nums)]
                    tt.sort()
                    nums[index_a+1:len(nums)] = tt
                    return nums
                index_b -= 1
            index_a -= 1
        nums.reverse()
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.nextPermutation(nums = [1,3,2]))