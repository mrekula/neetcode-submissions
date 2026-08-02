class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # res = 0

        # for i in range(len(heights)):
        #     temp = heights[i]*1
        #     temp_l = heights[i]
        #     for j in range(i+1, len(heights)):
        #         temp_l = min(temp_l,heights[j] )
        #         temp = max(temp, (j-i+1)*temp_l)
        #         print(temp_l,temp,i,j )
        #     res = max(res, temp)
        # return res

## stack

        max_area = 0
        stack =[]

        for i,h in enumerate(heights):
            start = i
            while stack and h < stack[-1][1]:
                index, height = stack.pop()
                max_area = max(max_area,height*(i-index))
                start = index
            stack.append((start,h))
        for i,h in stack:
            max_area = max(max_area,h* (len(heights)-i))
        return max_area








        