class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:


       
        rows = len(matrix)
        columns = len(matrix[0])
        
        l =-1
        h = rows
         # first figure out the row
        while h-l >1:
            m = ( h+l)//2
            if matrix[m][0] <= target:
                l = m
            else:
                h = m
        final_row = l
        print(final_row)

        # figure out columns

        l = -1
        h = columns

        while h-l > 1:
            m = (h+l)//2
            if matrix[final_row][m] < target:
                l =m
            else:
                h =m
        print(h)
        return True if h < columns and matrix[final_row][h]==target else False
