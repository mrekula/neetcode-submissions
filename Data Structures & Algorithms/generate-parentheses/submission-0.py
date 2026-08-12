class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res =[]

        def dfs(open, closed, subset):
            if closed > open or closed > n or open > n:
                return
            if closed == open and len(subset) == 2*n:
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




        