class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:


        stack=[]
        res=[0]*len(temperatures)

        for index,temp in enumerate(temperatures):

            while stack and temp > stack[-1][0]:
                old_temp, old_index= stack.pop()
                res[old_index]= index-old_index
            stack.append([temp,index])
        return res



        