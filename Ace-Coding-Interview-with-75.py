from typing import List

# Merge Strings Alternately
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        i, j = 0, 0
        res = ""
        while i < len(word1) and j < len(word2):
            res += word1[i] + word2[j]
            i += 1
            j += 1

        # add the additional letter before
        res += word1[i:] + word2[j:]
        return res

    def gcdOfStrings(self, str1: str, str2: str) -> str:
        len1, len2=len(str1),len(str2)

        def divisor(l):
            if len1 % l or len2 % l:
                return False
            f1,f2=len1//l,len2//l
            return str1[:l]*f1==str1 and str1[:l]*f2==str2

        for l in range(min(len1,len2),0,-1):
            if divisor(l):
                return(str1[:l])
        return ""
    
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = max(candies)
        return [i+extraCandies >= greatest for i in candies]

    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if not n:
            return True
        i = len(flowerbed)
        while i > 0:
            i -= 1
            prev = flowerbed[i - 1] if i > 0 else 0
            next = flowerbed[i + 1] if i < len(flowerbed) - 1 else 0
            if not (prev or flowerbed[i] or next):
                if not (n := n - 1):
                    return True
                i -= 1
        return False

    def reverseVowels(self, s: str) -> str:
        s=list(s)
        n=len(s)
        left=0
        right=n-1
        # Use hashset can reduce to O(1) checking
        vowels=set('AEIOUaeiou')
        while left<right:
            while left<right and s[left] not in vowels:
                left+=1
            while left<right and s[right] not in vowels:
                right-=1
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
        s=''.join(s)
        return s
    
    # def reverseWords(self, s: str) -> str:
    #     return " ".join(reversed(s.split()))
    
    # https://builtin.com/data-science/pythonic
    def reverseWords(self, s: str) -> str:
        x = s.split()
        # Can change into below but the speed is in same way
        # python still need to store an intermediate variable
        # return " ".join(s.split()[::-1])
        return " ".join(x[::-1])
    
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix_products = [1] * n
        suffix_products = [1] * n
        answer = [1] * n

        # Calculate prefix products
        for i in range(1, n):
            prefix_products[i] = prefix_products[i - 1] * nums[i - 1]

        # Calculate suffix products
        for i in range(n - 2, -1, -1):
            suffix_products[i] = suffix_products[i + 1] * nums[i + 1]

        # Calculate answer
        for i in range(n):
            answer[i] = prefix_products[i] * suffix_products[i]

        return answer
    
    # Faster version
    # def productExceptSelf(self, nums: List[int]) -> List[int]:
    #     arr = [1] * (len(nums))
    #     pre_product = 1
    #     for i in range(len(nums)):
    #         arr[i] *= pre_product
    #         pre_product *= nums[i]
        
    #     post_product = 1
    #     for i in range(len(nums)-1, -1, -1):
    #         arr[i] *= post_product
    #         post_product *= nums[i]

    #     return arr

    # Faster version
    # def increasingTriplet(self, nums: List[int]) -> bool:
    #     first = second = float('inf')
    #     for i in range(0, len(nums)):
    #         if  first >= nums[i]:
    #             first = nums[i]
    #         elif second >= nums[i]:
    #             second = nums[i]
    #         else:
    #             return True
    #     return False
    
    def increasingTriplet(self, nums: list[int]) -> bool:
        first, second = float('inf'), float('inf')
        for third in nums:
            if second < third: 
                return True
            if third <= first: 
                first= third    
            else:  
                second = third 
        return  False

if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.productExceptSelf([1,2,3,4]))  # Output: "world hello"
