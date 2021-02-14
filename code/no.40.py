class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        核心思想：
                分析题目同样可以看出我们应该使用回溯法进行求解
                去重的关键在于，若当前循环中的i等l则跳过
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
        candidates.sort()
        result = []
        temp = candidates[0] - 1

        def backtrack(target, candidates, temp, result, path, start):
            for i in range(start, len(candidates)):
                if candidates[i] == temp:
                    continue
                path.append(candidates[i])
                if sum(path) < target:
                    backtrack(target, candidates, temp, result, path, i + 1)
                elif sum(path) == target:
                    result.append(path[:])
                    path.pop()
                    return
                else:
                    path.pop()
                    return
                temp = path.pop()
        backtrack(target, candidates, temp, result, [], 0)
        # print(result)
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
