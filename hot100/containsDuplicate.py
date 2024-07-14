from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        the_set = set()
        for num in nums:
            if num in the_set:
                return True
            the_set.add(num)
        return False
    
if __name__ == '__main__':
    solution_instance = Solution()
    print(solution_instance.containsDuplicate([1,2,3,1]))