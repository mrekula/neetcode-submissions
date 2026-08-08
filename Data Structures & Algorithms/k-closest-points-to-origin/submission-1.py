class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap =[]
        for i in range(len(points)):
            dist = (points[i][0]-0)**2+ (points[i][1]-0)**2
            heapq.heappush(heap,[-dist, points[i]])
            while len(heap) > k:
                heapq.heappop(heap)

        return [j for i,j in heap]





        