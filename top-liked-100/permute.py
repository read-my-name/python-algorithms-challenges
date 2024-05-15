from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def find_permutations(nums):
            # Base case: If the list is empty, return a list containing an empty list
            if len(nums) == 0:
                return [[]]

            # The list to store all permutations
            permutations = []

            # Iterate through all numbers in the list
            for i in range(len(nums)):
                # Remove the i-th element
                num = nums[i]
                remaining_nums = nums[:i] + nums[i+1:]
                
                # Recursive step: Get all permutations of the remaining list
                for perm in find_permutations(remaining_nums):
                    # Prepend the removed element and add the new permutation to the list
                    permutations.append([num] + perm)
                    
            return permutations
    
        return find_permutations(nums)
    
if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.permute([1, 2, 3]))  # Call the permute method with the given input