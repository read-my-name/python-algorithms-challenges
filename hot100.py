from typing import List, Optional

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pair_idx = {}

        for i, num in enumerate(nums):
            if target - num in pair_idx:
                return [i, pair_idx[target - num]]
            pair_idx[num] = i

    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     dummyHead = ListNode(0)
    #     tail = dummyHead
    #     carry = 0

    #     while l1 is not None or l2 is not None or carry != 0:
    #         digit1 = l1.val if l1 is not None else 0
    #         digit2 = l2.val if l2 is not None else 0

    #         sum = digit1 + digit2 + carry
    #         digit = sum % 10
    #         carry = sum // 10

    #         newNode = ListNode(digit)
    #         tail.next = newNode
    #         tail = tail.next

    #         l1 = l1.next if l1 is not None else None
    #         l2 = l2.next if l2 is not None else None

    #     result = dummyHead.next
    #     dummyHead.next = None
    #     return result
    
    # Faster Version
    # def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    #     dummy = ListNode()
    #     res = dummy

    #     total = carry = 0

    #     while l1 or l2 or carry:
    #         total = carry

    #         if l1:
    #             total += l1.val
    #             l1 = l1.next
    #         if l2:
    #             total += l2.val
    #             l2 = l2.next

    #         num = total % 10
    #         carry = total // 10
    #         dummy.next = ListNode(num)
    #         dummy = dummy.next
        
    #     return res.next

    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     seen = {}
    #     l = 0
    #     length = 0
    #     for r in range(len(s)):
    #         char = s[r]
    #         if char in seen and seen[char] >= l:
    #             l = seen[char] + 1
    #         else:
    #             length = max(length, r - l + 1)
    #         seen[char] = r

    #     return length
    
    # Faster Version
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        maxlength=0
        l=0
        for r in range(len(s)):
            if s[r] not in charset:
                charset.add(s[r])
                maxlength = max(maxlength, r-l+1)
            else:
                while s[r] in charset:
                    charset.remove(s[l])
                    l+=1
                charset.add(s[r])
        return maxlength

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        nums1.extend(nums2)
        nums1.sort()
        m=len(nums1)//2
        if len(nums1)%2!=0:
            return nums1[m]
        else:
            return (nums1[m-1]+nums1[m])/2
        
    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     merged_list = nums1 + nums2
    #     merged_list.sort()
    #     merged_length = len(merged_list)
   
    #     if (merged_length % 2 == 0):
    #         #index starts from 0
    #         half = int(merged_length / 2 - 1)
    #         return (merged_list[half] + merged_list[half + 1]) / 2
    #     else:
    #         #index starts from 0
    #         half = int((merged_length // 2))
    #         return merged_list[half]

    # sort function is faster than quicksort
    # def quicksort(self, nums):
    #     if len(nums) <= 1:
    #         return nums
    #     pivot = nums[len(nums) // 2]
    #     left = [x for x in nums if x < pivot]
    #     mid = [x for x in nums if x == pivot]
    #     right = [x for x in nums if x > pivot]

    #     return self.quicksort(left) + mid + self.quicksort(right)

    # def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
    #     nums1.extend(nums2)
    #     nums1 = self.quicksort(nums1) 

    #     m=len(nums1)//2
    #     if len(nums1)%2!=0:
    #         return nums1[m]
    #     else:
    #         return (nums1[m-1]+nums1[m])/2

    def longestPalindrome(self, s: str) -> str:
        if s[::-1] == s:
            return s
        
        # inti start at 0 and window size is 1
        start, size = 0, 1

        for i in range(1, len(s)):
            # set up l, r pointer , base on cur idx to left
            # cur window size = max window size + 1
            l, r = i - size, i + 1

            # cur window size = max window size + 2
            s1 = s[l-1:r]

            # if s1 is palindrome, update start idx and the size
            if l >= 1 and s1[::-1] == s1:
                size += 2
                start = l - 1
            else:
                # cur window size = max window size + 1
                s2 = s[l:r]
                if s2[::-1] == s2:
                    size += 1
                    start = l
        
        return s[start:start+size]

if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.lengthOfLongestSubstring("pwwkew"))  # Output: "world hello"