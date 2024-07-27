class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for i in range(len(nums) - 2, -1, -1):
            if i + nums[i] >= goal:
                goal = i
        
        return True if goal == 0 else False
    
if __name__ == "__main__":
    nums = [2,3,1,1,4]
    print(Solution().canJump(nums))
    nums = [3,2,1,0,4]
    print(Solution().canJump(nums))


