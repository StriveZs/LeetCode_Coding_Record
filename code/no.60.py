from goto import with_goto
class Solution(object):
    # 计数菌
    jishuqi = 0
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str

        核心思想：这里Python有现成的库可以进行，但是为了能够掌握代码，这里我使用回溯法进行编写代码
                然后返回第k个结果

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
        nums = [i+1 for i in range(n)]
        def backtrack(nums,k):
            if self.jishuqi == k:
                return
            if not nums:  # 如果为空则表示选择完毕
                if nums in result:
                    return False
                else:
                    self.jishuqi += 1
                    result.append(temp[:])
                    return True
            for i in range(len(nums)):
                # 做出选择
                temp.append(nums[i])
                # 去除做出的选择
                tt = nums[:i] + nums[i + 1:]
                # 接着执行选择
                backtrack(tt,k)
                # 撤销选择
                temp.pop()

        backtrack(nums,k)
        res = ''
        for i in range(len(result[-1])):
            res += str(result[-1][i])
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.getPermutation(n=9,k=54994))