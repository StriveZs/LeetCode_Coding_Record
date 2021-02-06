class Solution(object):
    # 二分查找边界坐标 如果没有则返回[-1,-1]
    # 查找左侧边界
    def leftbinarySearch(self,nums,l,r,target):
        if nums[l] == target:
            if l == 0:
                return 0
            elif nums[l-1] != target:
                return l
            elif nums[l-1] == target:
                return self.leftbinarySearch(nums, l-1, r, target)
        elif r > l:
            mid = int((r+l)/2)
            if nums[mid] > target:
                return self.leftbinarySearch(nums, l, mid-1,target)
            elif nums[mid] < target:
                return self.leftbinarySearch(nums, mid+1, r, target)
            elif nums[mid] == target:
                return self.leftbinarySearch(nums, mid, r, target)
        else:
            return -1

    # 查找右侧边界
    def rightbinarySearch(self,nums,l,r,target):
        if nums[r] == target:
            if r == len(nums)-1:
                return len(nums)-1
            elif nums[r + 1] != target:
                return r
            elif nums[r + 1] == target:
                return self.rightbinarySearch(nums, l, r+1, target)
        elif r > l:
            mid = int((r + l) / 2)
            if nums[mid] > target:
                return self.rightbinarySearch(nums, l, mid - 1, target)
            elif nums[mid] < target:
                return self.rightbinarySearch(nums, mid + 1, r, target)
            elif nums[mid] == target:
                return self.rightbinarySearch(nums, l, mid, target)
        else:
            return -1

    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        核心思想：
            由于给定的数组是一个非递减数组，因IC同样可以使用33的中的二分法来查找到target的左右边界index
        例子：
            [5,7,7,8,8,8,10], target = 8
            左右边界点分别为3、5
        """
        if len(nums) == 0:
            return [-1,-1]
        a = self.leftbinarySearch(nums,0,len(nums)-1,target)
        b = self.rightbinarySearch(nums,0,len(nums)-1,target)
        boundarylist = []
        boundarylist.append(a)
        boundarylist.append(b)
        return boundarylist



if __name__ == '__main__':
    s = Solution()
    print(s.searchRange([5,7,7,8,8,10],8))