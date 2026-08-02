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
            d[num]= 1+ d.get(num,0)
        # create index:
        out = [[] for i in range(len(nums))]

        for key in d:
            out[d[key]-1].append(key)
        # pop index:

        output=[]
        for i in range(len(nums)-1, -1, -1):
            for j in out[i]:
                if len(output) < k:
                    output.append(j)
                else:
                    break
        return output

    


        

        