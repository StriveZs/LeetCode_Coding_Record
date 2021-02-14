class Solution(object):
    # 检查选择要填充的数字是否在一行/一列/九个格子里面出现
    def check(self, board, row, col, c):
        for i in range(9):
            if board[row][i] == c:
                return False
            if board[i][col] == c:
                return False
            if board[(row//3)*3 + i // 3][(col//3)*3 + i % 3] == c:
                return False
        return True

    # 回溯法
    def backtrack(self,board,i,j):
        # 停止条件
        ## 一行访问完之后跳转到下一行
        if j == 9:
            return self.backtrack(board,i+1,0)
        ## 所有行访问完之后，返回True
        if i == 9:
            return True
        ## 如果不为.，则不用管,继续访问下一列
        if board[i][j] != '.':
            return self.backtrack(board,i,j+1)

        # 选择操作
        ## 遍历选择列表，此处的选择是，给空白处填 "1" - "9" 中之一
        for k in range(1,10):
            c = str(k)
            if not self.check(board, i, j, c):  # 判断选择的字符是否满足要求（不与其他位置冲突）
                continue
            board[i][j] = c  # 做出选择
            if self.backtrack(board, i, j + 1):  # 递归调用，直接return是因为只需要一个可行解，而不需要所有可行解
                return True
            board[i][j] = '.'  # 撤销选择

    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        核心思想：采用回溯法

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
        self.backtrack(board,0,0)
        return board


if __name__ == '__main__':
    s = Solution()
    print(s.solveSudoku([["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))
