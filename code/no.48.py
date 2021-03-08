class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        核心思想:
                分析示例可以看出，我们如果先进性矩阵的转置，则可以得到目标结果的中心对称矩阵，然后在对该矩阵进行镜像
                即可以得到目标矩阵
        """
        n = len(matrix)
        # 先进行转置  行变列、列变黄
        for i in range(n):
            for j in range(n):
                # 仅进行对角交换即可
                if j > i:
                    t = matrix[i][j]
                    matrix[i][j] = matrix[j][i]
                    matrix[j][i] = t

        # 再进行镜像 中心轴对称变换
        center_axis = int(n/2) # 中心轴对应的下标
        for i in range(n):
            for j in range(n):
                if j < center_axis:
                    t = matrix[i][j]
                    matrix[i][j] = matrix[i][n-j-1]
                    matrix[i][n - j - 1] = t



if __name__ == '__main__':
    s = Solution()
    s.rotate(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])