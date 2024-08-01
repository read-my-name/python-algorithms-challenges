from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # min_value = min(nums)
        # max_value = max(nums)
        # count = [0] * (max_value - min_value + 1)

        # for num in nums:
        #     count[num - min_value] += 1
        
        # remain = k
        # for num in range(len(count) -1, -1, -1):
        #     remain -= count[num]
        #     if remain <= 0:
        #         return num + min_value
        
        # 2nd approach
        largest = float('-inf')
        for num in nums:
            if num > largest:
                largest = num
        freq = {}
        for num in nums:
            diff = largest - num
            if diff in freq:
                freq[diff] += 1
            else:
                freq[diff] = 1
        count = 0
        diff = 0
        while count < k:
            count += freq.get(diff, 0)
            diff += 1

        return largest - diff + 1

if __name__ == "__main__":
    nums = [3,2,1,5,6,4]
    k = 2
    print(Solution().findKthLargest(nums, k))