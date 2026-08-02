class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = []
        heapq.heapify(heap)
        for num in stones:
            heapq.heappush(heap, -num)
        while len(heap) > 1:
            max_1 =  heapq.heappop(heap)
            max_2 =  heapq.heappop(heap)
            if max_1 < max_2:
                heapq.heappush(heap,-1*( max_2 - max_1))
        heap.append(0)
        return abs(heap[0]) 


        

        