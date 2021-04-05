import copy
class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.

        核心思想：
                考虑可以先用字符串存储结果，再将字符串转换为list
                如果为0则字符串+'0'，如果为1，则在字符串记录当前最后一个0的位置处加'1'，为2的话则直接在末尾加'2'
        """
        resStr = ''
        index0 = -1
        for i in range(len(nums)):
            if nums[i] == 0:
                if index0 == -1:
                    index0 = 0
                else:
                    index0 = index0 + 1
                resStr = '0' + resStr
            elif nums[i] == 1:
                resStr = resStr[0:index0+1] + '1' + resStr[index0+1:]
            elif nums[i] == 2:
                resStr = resStr + '2'
        nums=copy.copy([ int(i) for i in list(resStr)])
        return nums

if __name__ == '__main__':
    s = Solution()
    print(s.sortColors([0,1,2]))