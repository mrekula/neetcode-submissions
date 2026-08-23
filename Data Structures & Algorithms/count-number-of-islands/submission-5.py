class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows, cols = len(grid), len(grid[0])

        def neighbourHelper(r,c):
            neighbours = []
            for dir in [(-1,0), (1,0), (0,1),(0,-1)]:
                new_row = r+ dir[0]
                new_col = c+ dir[1]
                neighbours.append((new_row, new_col))

            return neighbours
        que = deque([])
        visited = set()

        islands = 0


        for row in range(rows):
            for col in range(cols):
                if grid[row][col] =="1" and (row, col) not in visited:
                    que.append((row,col))
                    islands += 1
                    while len(que) >= 1:
                        node_row, node_col = que.popleft()
                        for neigh in neighbourHelper(node_row, node_col):
                            if 0 <= neigh[0] < rows and 0 <= neigh[1] < cols and grid[node_row][node_col] == "1" and (neigh[0],neigh[1]) not in visited:
                                que.append((neigh[0],neigh[1]))
                                visited.add((neigh[0],neigh[1]))
        return islands





