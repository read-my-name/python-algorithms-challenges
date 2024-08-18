from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums[:]]
        res = []
        for _ in range(len(nums)):            
            n = nums.pop(0)
            perms = self.permute(nums)

            for p in perms:
                p.append(n)
            
            res.extend(perms)
            nums.append(n)
        
        return res

if __name__ == "__main__":
    nums = [1,2,3]
    # print(Solution().permute(nums))
    nums = [0,1]
    print(Solution().permute(nums))
    # nums = [1]
    # print(Solution().permute(nums))
    