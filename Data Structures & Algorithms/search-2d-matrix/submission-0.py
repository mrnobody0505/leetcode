class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l = 0
        r = len(matrix) - 1
        target_row = 0
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0] > target:
                r = mid - 1
            else:
                target_row = mid
                l = mid + 1
        
        l = 0
        r = len(matrix[0]) - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] > target:
                r = mid - 1
            else:
                l = mid + 1
        
        return False
        
        


        