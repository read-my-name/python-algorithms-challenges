from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}

        for i, n in enumerate(nums):
          if n in d and abs(i - d[n]) <= k:
            return True
          else:
            d[n] = i
        
        return False
    
if __name__ == "__main__":
  sol = Solution()
  print(sol.containsNearbyDuplicate([1,2,3,1], 3)) # True
  print(sol.containsNearbyDuplicate([1,0,1,1], 1)) # True
  print(sol.containsNearbyDuplicate([1,2,3,1,2,3], 2)) # False
