class Solution(object):          
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        核心思想：
                分析题目同样可以看出我们应该使用回溯法进行求解, 注意要进行剪枝操作
        回溯法的标准框架
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
        def backtrack(target, candidates, temp, l, result):
            if sum(temp) == target:
                result.append(temp[:])
                # print(temp)
                return
            if target < sum(temp):
                return
            for i in range(l,len(candidates)):
                temp.append(candidates[i])
                if sorted(temp) in result:
                    temp.pop()
                    continue
                backtrack(target, candidates, temp, i,result)
                temp.pop()

        candidates.sort()
        backtrack(target,candidates,[],0,result)
        #print(result)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum(candidates = [2,3,6,7], target = 7))
