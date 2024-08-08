from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count, summ = 0, 0
        d = {0:1}
        for i in range(len(nums)):
            summ += nums[i]
            print("summ-k =", summ-k)
            if summ - k in d:
                count += d[summ - k]
            if summ in d:
                d[summ] += 1
            else:
                d[summ] = 1
            print("Dict: ", d, " Count: ", count)
        return count

# 560. Subarray Sum Equals K
if __name__ == "__main__":
    nums = [1,1,1]
    k = 2
    print(Solution().subarraySum(nums, k))
    