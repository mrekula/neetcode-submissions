class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # M is total area
        # time: O(M) iteratiion +O(M) dfs -- o(M)
        # space: O(M) can have stack overfloa if everything is 1 and len > 1000

        # rows = len(grid)
        # cols = len(grid[0])
        # max_area = 0
        # visited =set()


        # def dfs(r,c):
        #     if r >= rows or r < 0 or c >= cols or c < 0 or (r,c) in visited or grid[r][c] != 1:
        #         return 0
        #     visited.add((r,c))
        #     return (1+ dfs(r+1,c) + dfs(r-1,c)  + dfs(r,c+1) + dfs(r,c-1))


        # for r in range(rows):
        #     for c in range(cols):
        #         if grid[r][c] == 1 and (r,c) not in visited:
        #             max_area = max(max_area, dfs(r,c))
        # return max_area

        # BFS

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0
        visited =set()
        que = deque()

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1 and (r,c) not in visited:
                    que.append((r,c))
                    visited.add((r,c))
                    temp = 1
                    while que:
                        r, c = que.popleft()
                        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nr, nc = r + dr, c + dc
                            if  0 <= nr < rows and 0 <= nc < cols and (nr,nc) not in visited and grid[nr][nc] == 1:
                                que.append((nr,nc))
                                visited.add((nr,nc))
                                temp += 1
                    max_area = max(temp, max_area)
        return max_area



        