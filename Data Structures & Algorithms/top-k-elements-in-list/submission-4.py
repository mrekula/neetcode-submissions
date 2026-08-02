class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_dict={}
        

        for num in nums:
            num_dict[num]=num_dict.get(num,0)+1
        # heap=[]

        # for (key,value) in num_dict.items():
        #     heapq.heappush(heap, (value,key))
        #     if len(heap) > k:
        #         heapq.heappop(heap)
        # return [num for (freq,num) in heap]

        ## bucket sort:
        freq = [[] for i in range(len(nums))]

        for num, c in num_dict.items():
            freq[c-1].append(num)
            
        out=[]
        for i in range(len(nums)-1, -1, -1):
            for f in freq[i]:
                out.append(f)
                if len(out)==k:
                    return out

                
 
        

    









       

        


        