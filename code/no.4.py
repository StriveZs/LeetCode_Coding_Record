class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        #print(nums1)
        nums1.extend(nums2)
        #print(nums1)
        nums1.sort()
        length = len(nums1)

        if length == 1:
            return nums1[0]
        elif length == 0:
            return 0
        elif length % 2 == 0:
            index1 = int(length / 2)
            index2 = index1 - 1
            return (nums1[index1] + nums1[index2]) / 2
        elif length % 2 == 1:
            index = int((length / 2))
            return nums1[index]



if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([3],[1,2]))