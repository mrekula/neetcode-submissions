class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:

        def get_neighbours(r,c):

            neigh = []
            for dir in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dir[0], c + dir[1]
                neigh.append((nr,nc))
            return neigh


        

        q = deque([])
        visited = set()
        fresh = 0

        rows, cols = len(grid), len(grid[0])

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append((r,c))
                    visited.add((r,c))
        
        if fresh == 0:
            return 0

        steps = 0
        while q:
            if fresh == 0:
                return steps
            len_of_q = len(q)
            for _ in range(len_of_q):
                r, c = q.popleft()
                for nr ,nc in get_neighbours(r,c):
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1 and (nr,nc) not in visited:
                        q.append((nr,nc))
                        visited.add((nr,nc))
                        fresh -= 1
            steps += 1
        return -1



            
            
            




            
