class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        核心思想:
                对列表进行遍历，然后对大于等于0的正整数创建字典, 没出现的正整数键值对应的为1
                然后从1开始访问字典，如果当前键值不存在则为没有出现的最小的正整数
        """
        temp = []
        maxNum = -1 # 最大值正整数
        for i in range(len(nums)):
            if nums[i] > 0:
                temp.append(nums[i])
                if nums[i] > maxNum:
                    maxNum = nums[i]
        # 解决 最大正整数过大的情况
        if maxNum >= len(temp):
            maxNum = len(temp)
        # 解决无正整数的情况
        if temp == []:
            return 1
        keyList = [i for i in range(maxNum+2)]  # 键值列表
        valueList = []  # 键值对应值的列表
        for i in range(maxNum+2):
            if i not in temp:
                valueList.append(-1)
            else:
                valueList.append(i)

        numsDict = dict(zip(keyList,valueList)) # 对应的字典
        #print(numsDict)
        index = -1
        for i in range(1,maxNum+2):
            if numsDict[i] == -1:
                index = i
                break
        return index

if __name__ == '__main__':
    s = Solution()
    print(s.firstMissingPositive(nums = [1,2,3,10,2147483647,9]))
