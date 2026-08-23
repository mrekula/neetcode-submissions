class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def neighbours(r,c):
            neighbours = []
            for dir in [(-1,0), (1,0), (0,-1), (0,1)]:
                new_row = r + dir[0]
                new_col = c + dir[1]
                neighbours.append((new_row, new_col))
            return neighbours

        que = deque([])
        visited = set()
        max_len = 0

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1 and (row,col) not in visited:
                    temp_len = 1
                    que.append((row,col))
                    visited.add((row, col))
                    while len(que) >= 1:
                        r, c = que.popleft()
                        for nr, nc in neighbours(r,c):
                            if  0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr, nc) not in visited:
                                que.append((nr,nc))
                                visited.add((nr,nc))
                                temp_len += 1
                    max_len = max(max_len, temp_len)
        return max_len




