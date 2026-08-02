class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n= len(temperatures)
        out = [0]* n

        stack=[]

        for i, temp in enumerate(temperatures):
            if i==0:
                stack.append([i, temp])
            else:
                while stack and stack[-1][1] < temp:
                    i_prev, temp_prev = stack.pop()
                    out[i_prev] = i-i_prev
                stack.append([i, temp])
        return out

        