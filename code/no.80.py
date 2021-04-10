class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int

        核心思想：
                通过单指针加上条件判断实现
        """
        index = 0 # 删除重复之后序列的长度
        for i in range(len(nums)):
            # 如果新序列的长度小于2，则新元素的加入必然不会和前面的元素重复
            if index < 2:
                nums[index] = nums[i]
                index += 1
            # 排除上面情况之后，如果新元素加入，如果它不会前面两个元素的相同，即没有和它相同的两个元素（可能有1个或者0个）
            elif nums[i] != nums[index-2]:
                nums[index] = nums[i]
                index += 1

        return index

if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates(nums = [0,0,1,1,1,1,2,3,3]))