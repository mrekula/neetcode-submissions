class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:

        stack =[]
        max_area =0

        for i,h in enumerate(heights):
            if stack and h < stack[-1][1]:
                while  stack and h < stack[-1][1]:
                    prev_i, prev_h = stack.pop()
                    max_area = max(max_area, (i-prev_i)*prev_h)
                stack.append([prev_i, h])

            else:
                stack.append([i,h])
        while stack:
            i, h = stack.pop()
            max_area= max(max_area, (len(heights)-i)*h)
    
        return max_area



        