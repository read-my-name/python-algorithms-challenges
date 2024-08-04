class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s[::-1] == s:
            return s
        start, size = 0, 1
        for i in range(1, len(s)):
            left, right = i - size, i + 1
            s1 = s[left-1:right]

            if left >= 1 and s1[::-1] == s1:
                size += 2
                start = left - 1
            else:
                s2 = s[left: right]
                if s2[::-1] == s2:
                    size += 1
                    start = left
        return s[start:start + size]
    
if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.longestPalindrome("babad"))  # Output: "bab"
