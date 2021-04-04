class Solution(object):
    # 二分法
    def binarySearch(self, source, target, head, end):
        if head > end:
            return False
        mid = int((head + end)/2)
        if target == source[mid]:
            return True
        elif target > source[mid]:
            return self.binarySearch(source,target,mid+1,end)
        elif target < source[mid]:
            return self.binarySearch(source,target,head,mid-1)

    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool

        核心思想:
                可以先搜索目标数据可能在哪行，通过跟行首进行对比可得
                然后使用二分法进行搜索该行所有的元素，如果满足则返回true，否则返回false
        """
        for i in range(len(matrix)):
            if i == len(matrix)-1:
                return self.binarySearch(matrix[i],target,0,len(matrix[i])-1)
            else:
                if target >= matrix[i][0] and target < matrix[i+1][0]:
                    return self.binarySearch(matrix[i], target, 0, len(matrix[i])-1)
        return False

if __name__ == '__main__':
    s = Solution()
    # print(s.binarySearch([1,2,3,4,5],6,0,5-1))
    print(s.searchMatrix(matrix = [[1]], target = 3))