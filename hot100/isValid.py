class Solution:
    def isValid(self, s: str) -> bool:
        # def is_pair(last, cur):
        #     if last == "(" and cur == ")" or last == "{" and cur == "}" or last == "[" and cur == "]":
        #         return True
        #     return False
        # st = []

        # for i in range(len(s)):
        #     if st:
        #         last = st[-1]
        #         if is_pair(last, s[i]):
        #             st.pop()
        #             continue
        #     st.append(s[i])
        
        # return not st

        def is_pair(last, cur):
            if last == '[' and cur == ']' \
                or last == '{' and cur == '}' \
                or last == '(' and cur == ')':
                return True
            return False
        st = []
        for i in s:
            if st:
                if is_pair(st[-1], i):
                    st.pop()
                    continue
            st.append(i)
        return not st

if __name__ == "__main__":
    s = Solution()
    print(s.isValid("()"))
    print(s.isValid("()[]{}"))
    print(s.isValid("(]"))
    print(s.isValid("([)]"))
    print(s.isValid("{[]}"))
    print(s.isValid("(("))
