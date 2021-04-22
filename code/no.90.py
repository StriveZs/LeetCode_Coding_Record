import copy

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        核心思想：
                经典回溯法
                def backtrack(path, selected):
                    if 满足停止条件：
                        res.append(path)
                    for 选择 in 选择列表：
                        做出选择
                        递归执行backtrack
                            满足则return True
                        如果不满足要求就撤销选择
        魔改78题就可以了
        只需要对生成的结果进行排序，然后判断是否在集合中，如果出现则不行
        """
        res = []
        res.append([])
        numsLen = len(nums)
        temp = []

        def backtrack(temp, l, numsLen, length):
            # 停止条件
            if len(temp) == length:
                t_1 = sorted(temp)
                if t_1 not in res:
                    tt = copy.copy(t_1)
                    res.append(tt)
                    return

            for j in range(l + 1, numsLen):
                # 做出选择
                temp.append(nums[j])
                # 递归执行
                backtrack(temp, j, numsLen, length)
                # 撤销选择
                temp.pop()

        # 递归调用  length值不同
        for i in range(1, numsLen + 1):
            backtrack(temp, -1, numsLen, i)
        return sorted(res)

if __name__ == '__main__':
    s = Solution()
    print(s.subsetsWithDup([4,4,4,1,4]))