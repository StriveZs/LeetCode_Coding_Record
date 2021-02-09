class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        核心思想：
                实际就是一个大模拟
                分别进行如下判断如果有不满足的情况则结束判断，最坏时间复杂度情况就是判断全部情况
                1. 判断每行
                2. 判断每列
                3. 判断每个格子
                针对每行每列可以采用去掉所有"."然后set判断长度是否一致
        """
        nums = list(str(i) for i in range(1,10))
        # dictList = dict(zip(nums,[0 for i in range(10)]))
        # print(dictList)
        # 判断每行
        for i in range(9):
            dictList = dict(zip(nums,[0 for i in range(10)]))
            for j in range(9):
                if board[i][j] == '.':
                    continue
                dictList[board[i][j]] += 1
                if dictList[board[i][j]] >= 2:
                    return False

        # 判断每列
        for i in range(9):
            dictList = dict(zip(nums,[0 for i in range(10)]))
            for j in range(9):
                if board[j][i] == '.':
                    continue
                dictList[board[j][i]] += 1
                if dictList[board[j][i]] >= 2:
                    return False

        # 判断每个格子
        for i in range(9):
            dictList = dict(zip(nums, [0 for i in range(10)]))
            remainder = i % 3 # 余数
            consult = int(i / 3) # 商
            for j in range(3):
                for k in range(3):
                    if board[j+consult*3][k+remainder*3] == '.':
                        continue
                    dictList[board[j+consult*3][k+remainder*3]] += 1
                    if dictList[board[j+consult*3][k+remainder*3]] >= 2:
                        return False
        return True

if __name__ == '__main__':
    s = Solution()
    print(s.isValidSudoku([
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","5"]
]))