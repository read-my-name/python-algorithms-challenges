from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)  # Include an extra element for easier calculation
        max_area = 0
        
        for row in matrix:
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            
            # Calculate max area using histogram method
            stack = []
            for i in range(len(heights)):
                print("====================")
                print("heights: ", heights)
                print("i: ", i, "stack: ", stack)
                while stack and heights[i] < heights[stack[-1]]:
                    print("stack before: ", stack)
                    h = heights[stack.pop()]
                    print("stack after: ", stack)
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                    print("Inside of loop - h: ", h, "w: ", w, "max_area: ", max_area)
                #print("Outside of loop - h: ", h, "w: ", w, "max_area: ", max_area)
                stack.append(i)
                print("stack append", stack)
                print("====================")
            
        return max_area
    
if __name__ == "__main__":
    matrix = [
        ["1", "0", "0", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    solution = Solution()
    result = solution.maximalRectangle(matrix)
    print(result)  # Output: 6


