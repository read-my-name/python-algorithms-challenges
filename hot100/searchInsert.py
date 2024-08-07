from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

# 35. Search Insert Position   
if __name__ := '__main__':
    nums = [1,3,5,6]
    target = 5
    print(Solution().searchInsert(nums, target))
