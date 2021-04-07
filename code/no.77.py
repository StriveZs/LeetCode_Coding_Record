import copy
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]

        核心思想:
                经典回溯法
                def backtrack(path, selected):
                    if 满足停止条件：
                        res.append(path)
                    for 选择 in 选择列表：
                        做出选择
                        递归执行backtrack
                            满足则return True
                        如果不满足要求就撤销选择
        """

        res = [] # 结果存储
        numList = [i for i in range(1,n+1)]
        temp = []
        def backtrack(temp,i,length):
            # 停止条件
            if len(temp) == length:
                if temp not in numList:
                    tt = copy.copy(temp)
                    res.append(tt)
                    return

            for j in range(i+1,n):
                # 做出选择
                temp.append(numList[j])
                # 递归执行
                backtrack(temp,j,k)
                # 撤销选择
                temp.pop()
        backtrack(temp,-1,k)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4,2))
