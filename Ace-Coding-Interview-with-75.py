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