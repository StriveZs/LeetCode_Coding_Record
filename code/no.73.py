import numpy as np

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.

        核心思想：
                观察例子可以看出被变成0的值不会被判断为需要将其所在的行和列置为0
                可以考虑使用一个和输入矩阵对应大小的标志矩阵(用来表示当前访问的位置是本来0还是被变成0的 要进行区分，才能避免出现上述情况)
                然后就是依次遍历矩阵，当一个值等于0的之后，则把它所在行和列的值均变为0，并且修改对应的标志矩阵
        """
        row = len(matrix) # 行数
        colum = len(matrix[0]) # 列数
        flagMatrix = np.ones(shape=(row,colum),dtype=bool) # 标志矩阵
        # print(flagMatrix)
        for i in range(row):
            for j in range(colum):
                if flagMatrix[i][j] and matrix[i][j] == 0:
                    # 将所在行的所有元素均设为0
                    for k in range(colum):
                        # 去除本来就为0的情况
                        if matrix[i][k] == 0:
                            continue
                        matrix[i][k] = 0
                        flagMatrix[i][k] = False
                    # 将所在列的所有元素均设为0
                    for k in range(row):
                        # 去除本来就为0的情况
                        if matrix[k][j] == 0:
                            continue
                        matrix[k][j] = 0
                        flagMatrix[k][j] = False
        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.setZeroes(matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]))