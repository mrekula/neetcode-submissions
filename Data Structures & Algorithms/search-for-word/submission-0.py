class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:


        rows = len(board)
        cols = len(board[0])

        seen = set()

        def dfs(r,c,p):
            if p == len(word):
                return True
            if r >= rows or c >= cols or r < 0 or c < 0 or (r,c) in seen:
                return False
            if board[r][c] == word[p]:
                p += 1
                seen.add((r,c))
                res= dfs(r+1,c,p) or dfs(r-1,c,p) or dfs(r, c+1, p) or dfs(r, c-1,p)
                seen.remove((r,c))
                return res

        p =0
        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,p):
                    return True
        return False


  



            
        