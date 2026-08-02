class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # for row in range(len(matrix)):
        #     for col in range(len(matrix[0])):
        #         if matrix[row][col]==target:
        #             return True
        # return False

        mylist=[num for row in matrix for num in row]
        l, r =0, len(mylist)-1

        while l <= r:
            mid = (l+r)//2
            if target > mylist[mid]:
                l = mid+1
            elif  target < mylist[mid]:
                r = mid-1
            else:
                return True
        return False


    
        