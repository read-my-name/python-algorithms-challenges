class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        dp = [[] for _ in range(target + 1)]

        for c in candidates:
            #print("char: ", c)
            for i in range(c, target + 1):
                #print("target: ", target, "--dp: ", dp, "i: ", i , " Before")
                if i == c:
                    #print("i == c: ", i)
                    dp[i].append([c])
                for comb in dp[i - c]:
                    #print("comb: ", comb, "[c]: ", [c])
                    dp[i].append(comb + [c])
                #print("target: ", target, "--dp: ", dp, "i: ", i, "After")
        return dp[target]
    

if __name__ == '__main__':
    solution_instance = Solution()  # Create an instance of the Solution class
    print(solution_instance.combinationSum([2,3,6,7], 7))