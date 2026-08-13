class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        '''
        ( )) open  =1
        )   closed != open

        '''

        res =[]

        def dfs(open, closed, subset):

            if closed > open or open > n:
                return
            if closed == n and open == n:
                res.append(''.join(subset.copy()))
                return
            subset.append('(')
            dfs(open+1, closed, subset)
            subset.pop()
            subset.append(')')
            dfs(open, closed+1, subset)
            subset.pop()
        dfs(0,0,[])
        return res

        




        