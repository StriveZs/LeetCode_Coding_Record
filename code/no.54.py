class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        核心思想：正常采用由右→下→上→左→右的顺序访问即可
                由于-100 <= matrix[i][j] <= 100，因此可以将已经访问的过数字设置为101
                如果触碰到101或者超出边界，则重新调整方向
        """
        direction = 'right' # 方向初始为右，按照由右→下→上→左→右的顺序进行改变
        result = [] # 输出结果list
        num = 0 # 技术菌
        i,j = 0,0 # 初始坐标
        row = len(matrix) # 行数
        column = len(matrix[0]) # 列数
        sum = row * column # 矩阵元素总个数

        while num != sum:
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
            if matrix[i][j] == 101:
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
            t = matrix[i][j]
            result.append(t)
            matrix[i][j] = 101
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
        return result


if __name__ == '__main__':
    s = Solution()
    print(s.spiralOrder(matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]))