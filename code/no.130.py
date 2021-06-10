class Solution(object):
    # fixme: BFS
    def BFS(self,board, row, col):
        """
        :param board: List[List]棋盘
        :param row: Int 行
        :param col: Int 列
        :return: Boolean
        """
        row_limit, col_limit = len(board), len(board[0])
        # 检查越界情况
        if row < 0 or row >= row_limit or col < 0 or col >= col_limit:
            return
        if board[row][col] == 'O':
            board[row][col] = '#'
            # 上下左右查找
            self.BFS(board, row + 1, col)
            self.BFS(board, row - 1, col)
            self.BFS(board, row, col - 1)
            self.BFS(board, row, col + 1)
        return

    def solve(self, board):
        """
        考虑BFS，分析可得如果边界存在O的话，则可能会出现不能全部为X的情况，当然也存在边界为O，但是内部全为X的情况
        如果边界全为X的话，则必然最终结果全为X
        边界上O可到的的O均为不可以变为X的
        边界O上不可达的O均为可以变为X的
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        if len(board) == 0:
            return
        dim1,dim2 = len(board),len(board[0])
        # 从边界非X的开始查找  边界上O可到的的O均为不可以变为X的
        ## 上下边界
        for i in range(dim1):
            self.BFS(board, i, 0)
            self.BFS(board, i, dim2-1)
        ## 左右边界
        for j in range(dim2):
            self.BFS(board, 0, j)
            self.BFS(board, dim1-1, j)
        # 处理所有的# # 表示不可以变为X的
        for i in range(dim1):
            for j in range(dim2):
                if board[i][j] == '#':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
if __name__ == '__main__':
    s = Solution()
    print((s.solve(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]])))