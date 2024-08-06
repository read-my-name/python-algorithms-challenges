from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        print("nums: ", nums)
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            print(i)
            if i + nums[i] >= goal:
                goal = i
        return goal==0
        # return True if goal == 0 else False

# 55. Jump Game 
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))


