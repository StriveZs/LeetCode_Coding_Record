class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]

        核心思想：
                类似54题提到的访问方式
                首先要先将n×n的数组初始化全为0
                然后正常采用由右→下→上→左→右的顺序访问即可
                如果触碰到不为0的数或者超出边界，则重新调整方向
        """
        matrix = [] # 初始化数组
        for i in range(n):
            matrix.append([0 for i in range(n)])
        # print(matrix)
        direction = 'right' # 方向初始为右，按照由右→下→上→左→右的顺序进行改变
        num = 1 # 技术菌  从1开始到n^2结束
        i,j = 0,0 # 初始坐标
        row = len(matrix) # 行数
        column = len(matrix[0]) # 列数
        sum = row * column # 矩阵元素总个数

        while num <= sum:
            # 先处理超出边界情况:
            if i >= row: # 行数超了
                i -= 1
                j -= 1
                direction = 'left'
            elif i < 0: # 行数不够
                i += 1
                j += 1
                direction = 'right'
            elif j < 0: # 列数不够
                j += 1
                i -= 1
                direction = 'up'
            elif j >= column: # 列出超了
                j -= 1
                i += 1
                direction = 'down'

            # 在处理一下到达101的情况
            if matrix[i][j] != 0:
                if direction == 'right':
                    direction = 'down'
                    j -= 1
                    i += 1
                elif direction == 'down':
                    direction = 'left'
                    i -= 1
                    j -= 1
                elif direction == 'left':
                    direction = 'up'
                    j += 1
                    i -= 1
                elif direction == 'up':
                    direction = 'right'
                    i += 1
                    j += 1
            # 访问
            matrix[i][j] = num
            num += 1
            # 处理下标
            if direction == 'right':
                j += 1
            elif direction == 'down':
                i += 1
            elif direction == 'left':
                j -= 1
            elif direction == 'up':
                i -= 1
        return matrix

if __name__ == '__main__':
    s = Solution()
    print(s.generateMatrix(1))