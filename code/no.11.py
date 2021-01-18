class Solution(object):
    def maxArea(self, height):
        """
        从两头往中间靠，记录最佳
        :type height: List[int]
        :rtype: int
        """
        best = 0
        i = 0
        j = len(height) - 1
        while i < j:
            temp = (j - i) * min(height[i], height[j])  # 计算盛水容量
            if temp > best:
                best = temp
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return best


if __name__ == '__main__':
    s = Solution()
    print(s.maxArea([1,8,6,2,5,4,8,3,7]))
