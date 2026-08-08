class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        heap =[]
        for i in range(len(points)):
            dist = (points[i][0]-0)**2+ (points[i][1]-0)**2
            heap.append([-dist, i])
        heapq.heapify(heap)
        while len(heap) > k:
            heapq.heappop(heap)

        return [points[j] for i,j in heap]





        