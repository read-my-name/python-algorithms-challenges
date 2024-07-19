class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text2)
        
        prev = [0] * (n+1)
        for ch in text1:
            dp = [0] * (n+1)
            for i in range(n):
                if text2[i] == ch:
                    dp[i+1] = 1 + prev[i]
                else:
                    dp[i+1] = max(dp[i], prev[i+1])
            prev = dp
        return dp[-1]
    
if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonSubsequence('abced', 'ace'))
    print(solution.longestCommonSubsequence('abc', 'abc'))
    print(solution.longestCommonSubsequence('abc', 'def'))
    print(solution.longestCommonSubsequence('abc', 'defg'))
    print(solution.longestCommonSubsequence('abc', 'defgh'))
    print(solution.longestCommonSubsequence('abc', 'defghi'))
    print(solution.longestCommonSubsequence('abc', 'defghij'))
