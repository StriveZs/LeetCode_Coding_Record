class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]

        核心思想：这里Python有现成的库可以进行，但是为了能够掌握代码，这里我使用回溯法进行编写代码

        回溯法的框架：
            def backtrack(path, selected):
                if 满足停止条件：
                    res.append(path)
                for 选择 in 选择列表：
                    做出选择
                    递归执行backtrack
                        满足则return True
                    如果不满足要求就撤销选择
        """
        result = []
        temp = []
        def backtrack(nums):
            if not nums: # 如果为空则表示选择完毕
                if temp in result:
                    return
                else:
                    result.append(temp[:])
                    return
            for i in range(len(nums)):
                # 做出选择
                temp.append(nums[i])
                # 去除做出的选择
                tt = nums[:i]+nums[i+1:]
                # 接着执行选择
                backtrack(tt)
                # 撤销选择
                temp.pop()
        backtrack(nums)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.permuteUnique([1,2,3]))