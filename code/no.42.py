class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        核心思想:
                遍历找到最高点
                1. 从左往右到最高点，依次比较，如果左边的数大于右边的数，则表示能存到水
                2. 从右往左到最高点，依次比较，如果右边的数大于左边的数，则表示能存到水
                3. 大数则作为临时最大值，如果再有一个数大于大则更新临时最大数，临时最大数减去比他小的(左侧/右侧)数，则为能存的水数目
        """
        if height == []:
            return 0
        heightPoint = max(height) # 最高点
        heightIndex = height.index(heightPoint) # 最高点的下标
        length = len(height) # 列表长度
        # 先处理左边的
        leftVolum = 0
        leftmax = height[0]
        for i in range(0,heightIndex):
            temp = height[i]
            if height[i] <= leftmax:
                leftVolum += (leftmax - height[i])
            elif height[i] > leftmax:
                leftmax = height[i]

        # 然后处理右边的
        rightVolum = 0
        rightmax = height[length-1]
        for i in range(0,length - heightIndex):
            temp1 = height[length - i - 1]
            if height[length-i-1] <= rightmax:
                rightVolum += (rightmax - height[length-i-1])
            elif height[length-i-1] > rightmax:
                rightmax = height[length-i-1]
        #print(leftVolum)
        #print(rightVolum)
        return leftVolum + rightVolum

if __name__ == '__main__':
    s = Solution()
    print(s.trap(height = [4,2,0,3,2,5]))