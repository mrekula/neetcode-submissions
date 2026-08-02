class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict={}
        

        for num in nums:
            num_dict[num]=num_dict.get(num,0)+1
        heap=[]

        for (key,value) in num_dict.items():
                heapq.heappush(heap, (-value,key))
        out=[]
        for i in range(k):
            val, key=heapq.heappop(heap)
            out.append(key)
        return out
        

    









       

        


        