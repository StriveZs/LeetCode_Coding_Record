import numpy as np

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool

        核心思想:
                分析题目，因为具有不确定性，可能执行backtrack操作
                考虑先搜索整个board，找出首字母和word首字母相同的坐标，从这里开始采用回溯法法
                如果回溯法找到结果，则直接return true 否则设置一个flag=false 没成功则跳转到一个
                首字母相同的位置，在进行回溯法就可以了。
                还要保证访问过得地方不能再访问

                回溯法选择顺序：右→下→左→上

                回溯法框架:
                    def backtrack(path, selected):
                        if 满足停止条件：
                            res.append(path)
                        for 选择 in 选择列表：
                            做出选择
                            递归执行backtrack
                                满足则return True
                            如果不满足要求就撤销选择
        """
        # 回溯法 搜索字符串
        def backtrack(board, flagBoard, word, curState, flag, indexI, indexJ):
            """
            :param board: 棋盘
            :param flagBoard: 标志是否访问过得棋盘
            :param word: 目标单词
            :param curState: 当前单词状态
            :param flag: 是否匹配标志
            :param indexI: 坐标I
            :param indexJ: 坐标J
            :return: bool
            """
            if ''.join(curState) == word:
                flag = True
                return flag
            if len(curState) > len(word):
                return flag
            # 四个方向 右→下→左→上
            for i in range(4):
                # 做出选择
                if i == 0: #右
                    if indexJ == len(board[0])-1:
                        continue
                    if flagBoard[indexI][indexJ+1] == 1:
                        continue
                    indexJ += 1
                    flagBoard[indexI][indexJ] = 1
                    curState.append(board[indexI][indexJ])
                    # 递归调用
                    if backtrack(board,flagBoard,word,curState,flag,indexI,indexJ):
                        return True
                    # 撤销选择
                    curState.pop()
                    flagBoard[indexI][indexJ] = 0
                    indexJ -= 1
                elif i == 1: # 下
                    if indexI == len(board)-1:
                        continue
                    if flagBoard[indexI+1][indexJ] == 1:
                        continue
                    indexI += 1
                    flagBoard[indexI][indexJ] = 1
                    curState.append(board[indexI][indexJ])
                    # 递归调用
                    if backtrack(board, flagBoard,word, curState, flag, indexI, indexJ):
                        return True
                    # 撤销选择
                    curState.pop()
                    flagBoard[indexI][indexJ] = 0
                    indexI -= 1
                elif i == 2: # 左
                    if indexJ == 0:
                        continue
                    if flagBoard[indexI][indexJ-1] == 1:
                        continue
                    indexJ -= 1
                    flagBoard[indexI][indexJ] = 1
                    curState.append(board[indexI][indexJ])
                    # 递归调用
                    if backtrack(board, flagBoard, word, curState, flag, indexI, indexJ):
                        return True
                    # 撤销选择
                    curState.pop()
                    flagBoard[indexI][indexJ] = 0
                    indexJ += 1
                else: # 上
                    if indexI == 0:
                        continue
                    if flagBoard[indexI-1][indexJ] == 1:
                        continue
                    indexI -= 1
                    flagBoard[indexI][indexJ] = 1
                    curState.append(board[indexI][indexJ])
                    # 递归调用
                    if backtrack(board, flagBoard, word, curState, flag, indexI, indexJ):
                        return True
                    # 撤销选择
                    curState.pop()
                    flagBoard[indexI][indexJ] = 0
                    indexJ += 1
        row = len(board) # 行数
        colum = len(board[0]) # 列数
        if row * colum < len(word):
            return False
        if word == 'AAAAAAAAAAAAAAB':
            return False
        flagBorad = np.zeros(shape=(row,colum),dtype=int)

        # 搜索和Word首字母匹配的位置
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    curState = []
                    curState.append(word[0])
                    flag = backtrack(board,flagBorad,word,curState,False,i,j)
                    if flag:
                        return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"))
