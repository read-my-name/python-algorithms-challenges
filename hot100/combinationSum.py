from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        def make_combination(idx, comb, total):
            if total == target:
                res.append(comb[:])
                return
            if total > target or idx >= len(candidates):
                return
            comb.append(candidates[idx])
            make_combination(idx, comb, total + candidates[idx])
            comb.pop()
            make_combination(idx+1, comb, total)
        
        make_combination(0, [], 0)
        return res

# 39. Combination Sum
if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7
    print(Solution().combinationSum(candidates, target))
