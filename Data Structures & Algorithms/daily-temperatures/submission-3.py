class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        # out =[0] * len(temperatures)

        # for i in range(len(temperatures)):
        #     for  j in range(i+1, len(temperatures)):
        #         if temperatures[j] > temperatures[i]:
        #             out[i]=j-i
        #             break
        # return out
        res = [0] * len(temperatures)

        stack =[]

        for i, t in enumerate(temperatures):

            while stack and t > stack[-1][1]:
                index, prev_temp = stack.pop()
                res[index]= i- index
            stack.append((i,t))
        return res

            











        