class Solution(object):
    # 二分搜索
    def binarySearch(self,nums,start,ends,target):
        if ends < start:
            return False
        mid = int((start+ends)/2)
        if nums[mid] == target:
            return True
        else:
            if nums[mid] > target:
                return self.binarySearch(nums,start,mid-1,target)
            elif nums[mid] < target:
                return self.binarySearch(nums,mid+1,ends,target)

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool

        核心思想：
                考虑：寻找划分点，在这期间如果匹配到target则不用在查找了直接返回True
                    如果没找到，则直接将划分点之后的数组进行二分查找即可。
        """
        if len(nums) == 1:
            if nums[0] != target:
                return False
            else:
                return True
        # 寻找旋转点
        for i in range(len(nums)):
            if i == 0:
                if nums[i] == target:
                    return True
            if nums[i] == target: # 直接匹配到情况
                return True
            elif nums[i] < nums[i-1]:
                return self.binarySearch(nums[i:],0,len(nums[i:])-1,target)
        return self.binarySearch(nums,0,len(nums)-1,target) # 单独处理全是相同数字的情况

if __name__ == '__main__':
    s = Solution()
    #print(s.binarySearch([1,2,3,4],0,3,1))
    print(s.search(nums = [3,1], target = 0))
