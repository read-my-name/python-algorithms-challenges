from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        used = defaultdict(int)
        maxlen, start = 0, 0
        # i = index, c = char
        for i, c in enumerate(s):
            # start <= used[c] is to check the recently occurence
            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                maxlen = max(maxlen, i - start + 1)
            used[c] = i
        return maxlen
    
if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.lengthOfLongestSubstring("tmmzuxt"))