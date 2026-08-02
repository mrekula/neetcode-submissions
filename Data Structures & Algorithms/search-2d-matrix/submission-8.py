class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        if not matrix:
            return False

       
        l, r = -1, len(matrix)
        while r -l > 1:
            mid = (l+r)//2
            if matrix[mid][-1] == target:
                return True
            elif matrix[mid][-1] < target:
                l = mid
            else:
                r = mid
        row = r

        if row == len(matrix):
            return False

        l, r = -1, len(matrix[0])


        while r-l > 1:
            mid = (l+r)//2
            if matrix[row][mid] == target:
                return True
            elif matrix[row][mid] < target:
                l = mid
            else:
                r = mid
        return False

        