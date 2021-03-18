class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        
        核心思想：
                就是no.56的变形，只需要在开头把需要插入的区间添加到列表中
                然后在进行56题的操作即可
                依次判断:
                 1. 有交集且全包含的情况 A包含B和B包含A
                 2. 有交集且左包含的情况 [1,4] [0,1]  这个可以先对初始情况进行排序来解决
                 3. 有交集且右包含的情况 [0,2] [1,3]
                 3.如果两个区间没有交集，则放入result
        """
        intervals.append(newInterval)
        intervals = sorted(intervals)
        result = []
        temp = intervals[0]
        i = 1
        while i < len(intervals):
            # 有交集且全包含的情况 A包含B
            if temp[0] >= intervals[i][0] and temp[1] <= intervals[i][1]:
                temp = intervals[i]
                i += 1
            # 有交集且全包含的情况 B包含A
            elif temp[0] <= intervals[i][0] and temp[1] >= intervals[i][1]:
                i += 1
            # 有交集且右包含
            elif temp[1] >= intervals[i][0]:
                tt = []
                tt.append(temp[0])
                tt.append(intervals[i][1])
                temp = tt
                i += 1
            else:  # 下一个
                result.append(temp)
                temp = intervals[i]
                i += 1
        result.append(temp)
        return result

if __name__ == '__main__':
    s = Solution()
    print(s.insert(intervals = [[1,3],[6,9]], newInterval = [2,5]))