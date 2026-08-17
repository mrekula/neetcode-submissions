class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        bag =deque()
        fresh = 0
        rows = len(grid)
        cols = len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    bag.append((r,c))
        if fresh == 0:
            return 0
        timer = 0
        while bag and fresh > 0:
            length = len(bag)
            for _ in range(length):
                row, col = bag.popleft()
                for dr, dc in [(-1,0), (1,0), (0,1), (0,-1)]:
                    nr, nc = row + dr, col + dc
                    if  0 <= nr < rows  and 0 <= nc < cols and grid[nr][nc] == 1:
                        fresh -= 1
                        grid[nr][nc] = 2
                        bag.append((nr, nc))
            timer += 1
        return -1 if fresh > 0 else timer
            
            
            




            
