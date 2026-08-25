class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        def get_neighbours(r,c):
            neigh = []
            for dir in [(-1,0), (1,0), (0,-1), (0,1)]:
                nr, nc = r + dir[0], c + dir[1]
                neigh.append((nr,nc))
            return neigh
        
        rows, cols = len(heights), len(heights[0])
        pacific, atlantic = [],[]

        for r in range(rows):
            pacific.append((r, 0))
            atlantic.append((r,cols-1))
        for c in range(cols):
            pacific.append((0, c))
            atlantic.append((rows-1,c))
        pac = set()
        atl = set()

        def bfs(ocean, visited):
            q = deque(ocean)
            while q:
                len_of_q = len(q)
                for _ in range(len_of_q):
                    r, c = q.popleft()
                    visited.add((r,c))
                    for nr, nc in get_neighbours(r,c):
                        if 0 <= nr < rows and 0 <= nc < cols and heights[nr][nc] >= heights[r][c] and (nr,nc) not in visited:
                            q.append((nr,nc))
            return visited

        pacific_set = bfs(pacific, pac)
        atlantic_set = bfs(atlantic, atl)

        res = []

        for r in range(rows):
            for c in range(cols):
                if (r,c) in pacific_set and (r,c) in atlantic_set:
                    res.append((r,c))
        return res
        
        




        
        