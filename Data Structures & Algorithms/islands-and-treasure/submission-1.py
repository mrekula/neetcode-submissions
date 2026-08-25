class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        rows, cols = len(grid), len(grid[0])


        def neighbours(r, c):
            neigh = []
            for dir in [(-1,0), (1,0), (0,1), (0,-1)]:
                new_row , new_col = r + dir[0], c + dir[1]
                neigh.append((new_row, new_col))
            return neigh

        visited = set()
        q = deque([])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append((r,c))
                    visited.add((r,c))
    # if len(q) == 0:
    #     return False
        steps = 0

        while q:
            length_of_q = len(q)
            for _  in range(length_of_q):
                pop_r, pop_c = q.popleft()
                if grid[pop_r][pop_c] == 2147483647 :
                    grid[pop_r][pop_c] = steps

                for (nr, nc) in neighbours(pop_r, pop_c):
                    if  0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] != -1 and (nr,nc) not in visited:
                        visited.add((nr,nc))
                        q.append((nr,nc))
            steps += 1
                







        