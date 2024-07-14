import random
from typing import List

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        pivot = random.choice(nums)

        left, mid, right = [], [], []
        for n in nums:
            if n > pivot:
                right.append(n)
            elif n < pivot:
                left.append(n)
            else:
                mid.append(n)

        return self.sortArray(left) + mid + self.sortArray(right)
    
if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.sortArray([5,3,2,1]))