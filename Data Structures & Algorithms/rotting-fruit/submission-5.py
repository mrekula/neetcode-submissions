class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:


        # rows = len(grid)
        # cols = len(grid[0])
        # visited = set()
        # time = 0


        # def dfs(r,c, timer):

        #     if r < 0 or r >= rows or c < 0 or c >= cols or (r,c) in visited or grid[r][c] == 0:
        #         return 0
        #     if  grid[r][c] == 1:
        #         visited.add((r,c))
        #         timer += 1
        #     return 1+ dfs(r-1,c, timer), dfs(r+1,c, timer), dfs(r,c-1, timer),dfs(r,c+1, timer))


        rows = len(grid)
        cols = len(grid[0])
        fresh = 0
        que = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    que.append((r,c))
        timer = 0
        print(que)

        while que and fresh > 0:
            length = len(que)
            for _ in range(length):
                row, col = que.popleft()
                print(row, col)
                for dr, dc in [(1,0), (-1,0), (0,-1), (0,1)]:
                    nr = row + dr
                    nc = col + dc
                    print(nr, nc)
                    if  0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        # print(grid)
                        que.append((nr,nc))
                        fresh -= 1
            timer += 1
        return timer if fresh ==0 else -1

            
