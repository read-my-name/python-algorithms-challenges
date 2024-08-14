from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        
        # def quicksort(arr):
        #     if len(arr) <= 1:
        #         return arr
        #     else:
        #         mid = arr[len(arr) // 2]
        #         left = [x for x in arr if x < mid]
        #         middle = [x for x in arr if x == mid]
        #         right = [x for x in arr if x > mid]
        #         return quicksort(left) + middle + quicksort(right)
        # nums1 = quicksort(nums1)

        m=len(nums1)//2
        if len(nums1)%2!=0:
            return nums1[m]
        else:
            return (nums1[m-1]+nums1[m])/2

# 4. Median of Two Sorted Arrays      
if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.findMedianSortedArrays([1,3],[2]))