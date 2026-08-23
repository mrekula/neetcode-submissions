class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def neighbourHelper(r,c):

            neighbours =[]

            for direction in [(-1,0), (1,0), (0,1), (0,-1)]:
                new_row = r + direction[0]
                new_col = c + direction[1]
                neighbours.append((new_row, new_col))
            return neighbours

        que = deque([])
        visited = set()
        islands = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r,c) not in visited:
                    que.append((r,c))
                    islands += 1
                    while len(que) >= 1:
                        r, c = que.popleft()
                        neighbours = neighbourHelper(r,c)
                        for neighbour in neighbours:
                            if 0 <= neighbour[0] < rows and 0 <= neighbour[1] < cols and grid[neighbour[0]][neighbour[1]] == "1" and (neighbour[0], neighbour[1]) not in visited:
                                que.append((neighbour[0], neighbour[1]))
                                visited.add((neighbour[0], neighbour[1]))
        return islands




