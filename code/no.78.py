import copy
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        核心思想:
                同样是回溯法的应用
                相比较于上一题只不过是：k是可变的
                算法框架：
                    def backtrack(path, selected):
                        if 满足停止条件：
                            res.append(path)
                        for 选择 in 选择列表：
                            做出选择
                            递归执行backtrack
                                满足则return True
                            如果不满足要求就撤销选择
        """
        res = []
        res.append([])
        numsLen = len(nums)
        temp = []
        def backtrack(temp,l,numsLen,length):
            # 停止条件
            if len(temp) == length:
                if temp not in res:
                    tt = copy.copy(temp)
                    res.append(tt)
                    return

            for j in range(l+1,numsLen):
                # 做出选择
                temp.append(nums[j])
                # 递归执行
                backtrack(temp,j,numsLen,length)
                # 撤销选择
                temp.pop()
        # 递归调用  length值不同
        for i in range(1,numsLen+1):
            backtrack(temp, -1, numsLen,i)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.subsets(nums = [0]))