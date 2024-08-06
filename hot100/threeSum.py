from typing import List
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # nums.sort()
        # for i, a in enumerate(nums):
        #     if a > 0:
        #         break
        #     if i > 0 and a == nums[i - 1]:
        #         continue 
        #     l, r = i + 1, len(nums) - 1
        #     while l < r:
        #         threeSum = a + nums[l] + nums[r]
        #         if threeSum > 0:
        #             r -= 1
        #         elif threeSum < 0:
        #             l += 1
        #         else:
        #             res.append([a, nums[l], nums[r]])
        #             l += 1
        #             r -= 1
        #             while nums[l] == nums[l - 1] and l < r:
        #                 l += 1
        # return res

        res = []
        nums.sort()
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1

                    while nums[j] == nums[j-1] and j < k:
                        j += 1
        return res
    
# 15. 3Sum  
if  __name__ == "__main__":
    sol = Solution()
    print(sol.threeSum([-1,0,1,2,-1,-4]))
    print(sol.threeSum([]))
    print(sol.threeSum([0]))
    print(sol.threeSum([0,0,0,0]))
    print(sol.threeSum([0,0,0,0,0]))
    print(sol.threeSum([0,0,0,0,0,0]))
