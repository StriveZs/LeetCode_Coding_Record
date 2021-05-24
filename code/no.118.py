class Solution(object):
    res = []  # 全局结果

    # fixme: 递归分治生成数组
    def genrate_iList(self, pre_list, depth, goal_depth):
        """
        采用递归分治的方法来生成每一层的数组
        :param pre_list: List 上一层生成的数组
        :param depth: Int 当前深度
        :param goal_depth: Int 目标深度
        :return:
        """
        if depth == goal_depth + 1:
            return
        temp = []
        temp.append(1)
        for i in range(len(pre_list) - 1):
            temp.append(pre_list[i] + pre_list[i + 1])
        temp.append(1)
        self.res.append(temp)

        # 递归调用
        self.genrate_iList(temp, depth + 1, goal_depth)

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]

        核心思想：
            由于每个值都是它上面两个值的加和，因此考虑为分治问题
            考虑还是使用递归的方法，因此每次传入的数组就是上一次递归生成的数组.
        """
        self.res = []
        if numRows == 0:
            return self.res
        self.res.append([1])
        if numRows == 1:
            return self.res
        self.res.append([1, 1])
        if numRows == 2:
            return self.res
        self.genrate_iList([1, 1], 3, numRows)
        return self.res

if __name__ == '__main__':
    s = Solution()
    print(s.generate(5))