from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad = {
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        arr = []
        def dfs(res,string):
            if not string:
                arr.append(res)
                return
            currNum = string[0]
            for i in range(len(keypad[currNum])):
                dfs(res+keypad[currNum][i],string[1:])
        if digits:
            dfs("",digits)
        return arr

if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
    # print(Solution().letterCombinations(""))
    # print(Solution().letterCombinations("2"))
    # print(Solution().letterCombinations("234"))
    # print(Solution().letterCombinations("2345"))


