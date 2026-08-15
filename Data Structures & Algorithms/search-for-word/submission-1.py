class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        rows = len(board)
        cols = len(board[0])
        p =0

        visited = set()

        def dfs(r,c,p):
            if p == len(word):
                return True
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or board[r][c] != word[p]:
                return
            visited.add((r,c))
            p += 1
            res = dfs(r-1,c,p) or dfs(r+1,c,p) or dfs(r, c-1,p) or dfs(r, c+1,p)
            visited.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[p]:
                    if dfs(r,c,0):
                        return True
        return False