from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(open, close,s):
            if len(s)==n*2:
                # print('3rd open', open, 'close', close, 's', s)
                res.append(s)
                return
            
            if open<n:
                # print('1st open', open, 'close', close, 's', s)
                dfs(open+1,close, s + '(')
                # print('1st open', open, 'close', close, 's', s, 'after')

            if close<open:
                # print('2nd open', open, 'close', close, 's', s)
                dfs(open, close+1, s + ')')
                # print('2nd open', open, 'close', close, 's', s, 'after')

        
        res=[]
        dfs(0,0,'')
        return res

if __name__ == '__main__':
    print('Uncoment the print in the code for better understanding')

    for i in range(2,5):
        print('n', i)


    # solution_instance = Solution()  # Create an instance of the Solution class
    # print(solution_instance.generateParenthesis(3))  # Call the Solution function and print the result of the function