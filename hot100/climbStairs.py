class Solution:
    def climbStairs1(self, n: int) -> int:
        distinct_ways = [0] * (n + 1)
        distinct_ways[0] = 1
        distinct_ways[1] = 1
        for step in range(2, n + 1):
            distinct_ways[step] = distinct_ways[step - 1] + distinct_ways[step - 2]
        return distinct_ways[-1]
    
    # recursive
    def climbStairs2(self, n: int) -> int:
        self.dp={}
        return self.ans(n)
    
    def ans(self,n):
        if n <= 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            if n not in self.dp:
                self.dp[n] = self.ans(n-1)+self.ans(n-2)
            return self.dp[n]

def main():
    solution = Solution()
    total_steps = 5  # Example: Number of steps in the staircase
    ways_to_climb = solution.climbStairs1(total_steps)
    print(f"Number of distinct ways to climb {total_steps} steps: {ways_to_climb}")

if __name__ == "__main__":
    main()
