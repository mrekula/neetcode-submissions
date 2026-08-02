class Solution:
    def maxArea(self, heights: List[int]) -> int:

        max_area = 0
        left =0
        right = len(heights)-1

        while left < right:
            temp_area = min(heights[right],heights[left])* (right-left)
            max_area= max(max_area, temp_area)
            if heights[right] > heights[left]:
                left += 1
            else:
                right -= 1
        return max_area




    



