import sys
class Solution(object):
    maxSum = sys.maxsize # 设置足底啊之
    def limit_dfs(self,triangle,j,iList,curSum,curDepth,depth):
        """
        :param triangle: List[List[Int]] 所有数值
        :param j: Int 上一个节点的纵坐标
        :param iList: List[Int] 当前节点所在的层
        :param curParam: Int 当前层之前的路径和
        :param curDepth: Int 当前深度
        :param depth: 最大深度
        :return:
        """
        t = iList[j]
        curSum += iList[j]
        if depth == curDepth:
            if curSum < self.maxSum:
                self.maxSum = curSum
            return
        self.limit_dfs(triangle, j, triangle[curDepth+1], curSum, curDepth+1, depth)
        if j+1 < len(triangle[curDepth+1]):
            self.limit_dfs(triangle, j+1, triangle[curDepth + 1], curSum, curDepth+1, depth)

    def minimumTotal(self, triangle):
        """
        核心思想:
            每个节点，只能访问它的[i+1][j]/[i+1][j+1] 两个节点
            考虑采用递归来判断, 有点类似限制二叉树的访问方法
        :type triangle: List[List[int]]
        :rtype: int 返回最大值
        """
        self.limit_dfs(triangle,0,triangle[0],0,0,len(triangle)-1)
        return self.maxSum
    def new_version(self,triangle):
        for i in range(len(triangle) - 1, 0, -1):
            for j in range(i):
                triangle[i - 1][j] += min(triangle[i][j], triangle[i][j + 1])
        return triangle[0][0]


if __name__ == '__main__':
    s = Solution()
    print(s.minimumTotal([[-1],[2,3],[1,-1,-3]]))