class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        stones = [-i for i in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
                h1 = abs(heapq.heappop(stones))
                h2 = abs(heapq.heappop(stones))
                if h1-h2 > 0:
                    heapq.heappush(stones,-(h1-h2))
        return 0 if len(stones) == 0 else abs(stones[0])





        

        