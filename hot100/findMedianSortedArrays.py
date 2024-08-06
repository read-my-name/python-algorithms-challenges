from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        m=len(nums1)//2
        if len(nums1)%2!=0:
            return nums1[m]
        else:
            return (nums1[m-1]+nums1[m])/2

# 4. Median of Two Sorted Arrays      
if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.findMedianSortedArrays([1,3],[2]))