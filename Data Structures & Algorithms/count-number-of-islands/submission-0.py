class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # m = r*c
        # time : O(M) * ? cause we are not resetting visited. OSo ideally iyts not **4 combinatons
        # space: O(M) ofpr hashset and O(M) for call stack : O(M)
        rows = len(grid)
        cols = len(grid[0])
        visited = set()
        islands = 0

        def dfs(r,c):
            if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] != "1":
                return
            visited.add((r,c))
            dfs(r+1, c) or  dfs(r-1, c) or dfs(r, c+1)  or dfs(r, c-1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    islands += 1
                    dfs(r,c)
        return islands
                



        