#
# @lc app=leetcode.cn id=167 lang=python
#
# [167] 两数之和 II - 输入有序数组
#

# @lc code=start
from math import fabs


class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        题目分析:
            题目要求:
                你所设计的解决方案必须只使用常量级的额外空间
                因为假设只存在只对应唯一的答案,所以可以用数组来存储
                而且要保证indexs1 < indexs2
                仅存在一个有效答案
            思路一：
                通过双循环来实现, 可能时间复杂度上会高
                在18/21个测试用例挂了，超时了
            思路二:
                因为数组是非递增排列的，考虑从大往小找
                并设置indexs统计数值相同的下标，如果当前相同数值不满足的话，直接从统计下标再开始
                为了减小时间复杂度而设计
        """
        # 思路一:
        '''
        for i in range(len(numbers)):
            for j in range(i+1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i+1,j+1]
        '''
        # 思路二: 双指针 第一个指针单遍循环 第二个指针用于找第二个下标
        indexs = len(numbers) - 1
        target1 = None
        while indexs >= 0:
            if target - numbers[indexs] != 0:
                if target - numbers[indexs] > 0:
                    sec = indexs + 1
                    target1 = target - numbers[indexs]
                    if target1 - numbers[0] < 0:
                        indexs -= 1
                        continue
                    for i in range(indexs):
                        if target1 - numbers[i] < 0:
                            indexs -= 1
                            break
                        if target1 - numbers[i] == 0:
                            return [i+1, sec]
                elif target - numbers[indexs] < 0:
                    sec = indexs + 1
                    if indexs == 51:
                        t = numbers[indexs]
                    target1 = target - numbers[indexs]
                    if target1 - numbers[0] < 0:
                        indexs -= 1
                        continue
                    for i in range(indexs):
                        if target1 - numbers[i] > 0:
                            indexs -= 1
                            break
                        if target1 - numbers[i] == 0:
                            return [i+1, sec]
                else:
                    indexs -= 1
            elif target == 0 and numbers[indexs] == 0:
                return [indexs,indexs+1]
            elif target != 0 and target - numbers[indexs] == 0:
                if 0 in numbers:
                    sec = numbers.index(0)
                    return [sec+1,indexs+1]
                else:
                    indexs -= 1
            else:
                indexs -= 1
        

            


            
                

# s = Solution()
# print(s.twoSum(numbers = [-1000,-1,0,1], target = 1))
# @lc code=end

