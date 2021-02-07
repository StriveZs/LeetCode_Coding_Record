class Solution(object):
    # 二分查找索引值
    def binarySearch(self,nums,l,r,target):
        if l < r:
            mid = int((r+l)/2)
            if nums[mid] < target:
                return self.binarySearch(nums,mid+1,r,target)
            elif nums[mid] > target:
                return self.binarySearch(nums,l,mid-1,target)
            else:
                return mid
        elif r == l:
            if nums[r] == target:
                return l
            else:
                return l
        else:
            return l

    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        核心思想:
            使用二分法查找目标值，如果找到则返回索引值，如果没找到，则返回和它最接近数值的坐标（小于它的）
        """
        index = self.binarySearch(nums,0,len(nums)-1,target)
        if nums[index] == target:
            return index
        else:
            if index >= int(0+len(nums)-1)/2:
                if target > nums[len(nums)-1]:
                    index = len(nums)
            else:
                if nums[index] > target:
                    pass
                else:
                    index += 1
        return index

if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1,3,5,7,9],10))