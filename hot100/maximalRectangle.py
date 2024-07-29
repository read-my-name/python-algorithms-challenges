from typing import List


class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0
        
        rows, cols = len(matrix), len(matrix[0])
        heights = [0] * (cols + 1)  # Include an extra element for easier calculation
        max_area = 0
        
        for row in matrix:
            print("=======================")
            # Update heights for the current row
            print("row: ", row)
            for i in range(cols):
                heights[i] = heights[i] + 1 if row[i] == '1' else 0
            print("heights: ", heights) 
            
            # Calculate max area using histogram method
            stack = []
            for i in range(len(heights)):
                print("i: ", i, "heights[i]: ", heights[i], "stack: ", stack)
                while stack and heights[i] < heights[stack[-1]]:
                    print("=== heights[i] < heights[stack[-1]]: ", heights[i], " < ", heights[stack[-1]])
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                    print("max_area: ", max_area, "h: ", h, "w: ", w)
                stack.append(i)
            print("=======================")
        
        return max_area
    
if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "0", "1", "1", "1"],
        ["1", "0", "0", "1", "0"]
    ]
    solution = Solution()
    result = solution.maximalRectangle(matrix)
    print(result)  # Output: 6


