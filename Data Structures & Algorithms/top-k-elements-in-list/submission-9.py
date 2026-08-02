class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # d ={}
        # for num in nums:
        #     d[num] = 1+ d.get(num,0)

        # heap = []

        # for key,val in d.items():
        #     heapq.heappush(heap, (val,key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [key for (val,key) in heap]

    ## BUcket sort
        d ={}
        for num in nums:
            d[num] = 1+ d.get(num,0)
        out =[[] for i in range(len(nums)+1)]
        for key,val in d.items():
            out[val].append(key)
        output=[]
        for i in range(len(nums), -1, -1):
            for j in out[i]:
                output.append(j)
                if len(output)==k:
                    return output


    


        

        