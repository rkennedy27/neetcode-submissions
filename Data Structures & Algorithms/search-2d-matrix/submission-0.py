class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        low, high = 0, (m * n - 1)

        while low <= high:
            midpoint = (low + high) // 2
            # change this next line:
            value = matrix[midpoint // n][midpoint % n]

            if value == target:
                return True
            elif value < target:
                low = midpoint + 1
            else:
                high = midpoint - 1

        return False
                    
