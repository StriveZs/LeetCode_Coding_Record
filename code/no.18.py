class Solution:
    def fourSum(self, nums, target):
        if len(nums) < 4:
            return []
        res = []
        nums = sorted(nums)
        for i in range(len(nums)-3):
            # 1) 去重复
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # 2) 剪枝第一处，因为i后面位置的元素是递增排序的。
            if nums[i] + 3*nums[i+1] > target:
                break
            # 3) 剪枝第二处，因为i后面位置的元素是递增排序的。
            if nums[i] + 3*nums[-1] < target:
                continue
            for j in range(i + 1, len(nums)-2):
                # 4) 去重复
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                # 5) 剪枝第三处
                if nums[i]+nums[j]+2*nums[j+1] > target:
                    break
                # 6) 剪枝第四处
                if nums[i]+nums[j]+2*nums[-1] < target:
                    continue
                low, high = j + 1, len(nums) - 1
                while low < high:
                    if nums[i] + nums[j] + nums[low] + nums[high] == target:
                        res.append([nums[i], nums[j], nums[low], nums[high]])
                        low, high = low + 1, high - 1
                        # 7) 去重复
                        while low < high and nums[low] == nums[low - 1]:
                            low += 1
                        # 8) 去重复
                        while low < high and nums[high] == nums[high + 1]:
                            high -= 1
                    if nums[i] + nums[j] + nums[low] + nums[high] > target:
                        high -= 1
                    if nums[i] + nums[j] + nums[low] + nums[high] < target:
                        low += 1
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.fourSum([1, 0, -1, 0, -2, 2],0))