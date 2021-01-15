import numpy as np

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        
        list_str = list(s)
        length = len(s)
        if numRows == 1:
            return s
        onePart = numRows + (numRows - 2) # 一个Z字形前半部分的字符个数
        numPart = int(length / onePart) + 1 # 总共多少个part
        #print(list_str)

        storeChart = np.zeros((numRows,numPart*numRows-1),dtype=np.string_) # 用来存储Z字形变换后的字符
        #print(storeChart)
        row = 0
        flag = False
        for i in range(length):  # 时间复杂度为O(len(s))
            if numRows == 2:  # 单独处理2这种情况
                if i % onePart == 0:
                    storeChart[i % onePart][row] = list_str[i]
                elif i % onePart == 1:
                    storeChart[i % onePart][row] = list_str[i]
                    row += 1
            elif i % onePart < numRows:
                if flag:
                    row += 1
                    flag = False
                storeChart[i % onePart][row] = list_str[i]
            elif i % onePart >= numRows:
                row += 1
                flag = True
                storeChart[onePart - i % onePart][row] = list_str[i]
        #print(storeChart)
        strList = storeChart.astype(np.str)
        result = ''
        for i in range(strList.shape[0]):
            for j in range(strList.shape[1]):
                if strList[i][j] != '':
                    result += str(strList[i][j])

        return result


        
        

if __name__ == '__main__':
    s = Solution()
    print(s.convert('ABCD',2))